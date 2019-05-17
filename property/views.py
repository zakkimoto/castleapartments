from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, reverse

from property.forms.property_form import PropertyCreateForm, PropertyUpdateForm, BuyerForm, CreditCardForm
from property.models import Property, PropertyImage
from buyer.models import BuyerSession
from seller.models import Seller
from user.models import UserImage


def _search_properties(search_term):
    print(search_term)

    BuyerSession( search_term=search_term).save()
    return Property.objects.annotate(
        search=SearchVector('streetname', 'description', 'address', 'country', 'price')
    ).all().filter(search=search_term, on_sale=True).order_by('streetname')



def filter(request):
    if request.method == 'GET':
        bedrooms = request.GET.get('bedrooms', '')
        bathrooms = request.GET.get('bathrooms', '')
        size = request.GET.get('size', '')
        city = request.GET.get('city', '')
        postal_code = request.GET.get('postal_code', '')
        property_type = request.GET.get('property_type', '')
        price = request.GET.get('price', '')
        order = request.GET.get('order')



        query = Q(on_sale=True)
        if postal_code:
            query &= Q(postal_code=postal_code)
        if bedrooms:
            query &= Q(bedrooms=bedrooms)
        if city:
            query &= Q(city=city)
        if bathrooms:
            query &= Q(bathrooms=bathrooms)
        if size:
            query &= Q(size=size)
        if property_type:
            query &= Q(property_type=property_type)
        if price:
            query &= Q(price=price)



        properties = Property.objects.filter(query).order_by(order)

        context = {'properties': properties}
        return render(request, 'property/index.html', context)
    else:
        return HttpResponseNotAllowed()


def search(request):
    if request.method == 'GET':
        if 'search_filter' in request.GET:
            search_filter = request.GET['search_filter']
            print(search_filter + "search filter")
            properties = [{
                'id': x.id,
                'streetname': x.streetname,
                'description': x.description,
                'firstImage': x.propertyimage_set.first().image,
                'country': x.country,
                'size': x.size,
                'bathrooms': x.bathrooms,
                'bedrooms': x.bedrooms,
                'price': x.price,
                'city': x.city,
                'postal_code': x.postal_code,
                'property_type': x.property_type,
                'order': x.order
            } for x in _search_properties(search_filter)]
            return JsonResponse({'data': properties})
    else:
        return HttpResponseNotAllowed()



def index(request):
    if request.method == 'GET':
        if 'search' in request.GET:
            search_term = request.GET['search']
            print(search_term)
            print('here')

            print(request)

            properties = _search_properties(search_term)
        else:
            print("hér")
            print(request)
            properties = Property.objects.filter(on_sale=True).order_by('streetname')

        context = {'properties': properties}
        return render(request, 'property/index.html', context)
    else:
        return HttpResponseNotAllowed()


def get_property_by_id(request, id):
    res = Seller.objects.filter(user_id=request.user.id).values_list('pk', flat=True)
    if request.user.is_authenticated:
        seller_id=res.values()[0]['id']
        return render(request, 'property/property_details.html', {
            'property': get_object_or_404(Property, pk=id),
            'prufa': seller_id
        })
    else:
        return render(request, 'property/property_details.html', {
            'property': get_object_or_404(Property, pk=id),
        })


@login_required
def create_property(request):
    if request.method == 'POST':
        form = PropertyCreateForm(data=request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            seller = Seller.objects.filter(user_id=request.user.id).first()
            property.seller = seller
            property.save()

            property_image = PropertyImage(image=request.POST['image'], property=property)
            property_image.save()
            property_image2 = PropertyImage(image=request.POST['image2'], property=property)
            property_image2.save()
            property_image3 = PropertyImage(image=request.POST['image3'], property=property)
            property_image3.save()
            property_image4 = PropertyImage(image=request.POST['image4'], property=property)
            property_image4.save()




            return redirect('created_successful')
    else:
        form = PropertyCreateForm()
    return render(request, 'property/create_property.html', {
        'form': form
    })


@login_required
def created_successful(request):

    if request.method == 'GET':
        return render(request, 'property/created_successful.html', dict())


@login_required
def delete_property(request, id):
    property = get_object_or_404(Property, pk=id)
    property.delete()
    return redirect('property-index')


@login_required
def update_property(request, id):
    instance = get_object_or_404(Property, pk=id)
    if request.method == "POST":
        form = PropertyUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('property_details', id=id)
    else:
        form = PropertyUpdateForm(instance=instance)
    return render(request, 'property/update_property.html', {
        'form': form,
        'id': id
    })


def buy_property(request, id):
    property = get_object_or_404(Property, pk=id)
    if request.method == "POST":

        if property.buyer:
            form = BuyerForm(data = request.POST, instance=property.buyer)
        else:
            form = BuyerForm(data=request.POST)

        if form.is_valid():
            buyer = form.save()
            property.buyer = buyer
            property.save()

            #return redirect('payment_property', id=id)
            return redirect(reverse('payment_property', args=[id]))
        else:
            return render(request, 'property/buy_property.html', {
                'form': form,
                'id': id
            })
    else:

        if property.buyer:
            form = BuyerForm(instance=property.buyer)
        else:
            form = BuyerForm()

    return render(request, 'property/buy_property.html', {
        'form': form,
        'id': id
    })

def payment_property(request, id):
    property = get_object_or_404(Property, pk=id)

    if request.method == "POST":

        if property.buyer.credit_card:
            form = CreditCardForm(data = request.POST, instance=property.buyer.credit_card)
        else:
            form = CreditCardForm(data = request.POST)

        if form.is_valid():
            print("valid")
            credit_card = form.save()
            buyer = property.buyer
            buyer.credit_card = credit_card
            buyer.save()
            return redirect(reverse('payment_review', args=[id, None]))
        else:
            print("not valid")
            context = {
                'form': form,
                'id': id}
    else:
        print("get")
        if property.buyer.credit_card:
            context = {
                'form': CreditCardForm(instance=property.buyer.credit_card),
                'id': id}
        else:
            context = {
                'form': CreditCardForm(),
                'id': id}

    return render(request, 'property/payment_property.html', context)


def payment_review(request, id, confirm):
    print('confirm ', confirm)
    property = get_object_or_404(Property, pk=id)

    if request.method == "POST":
        print('in POST')

        if confirm == "True":
            property.on_sale = False
            property.save()

            return redirect(reverse('payment_successful'))


        else:
            property.buyer.credit_card.delete()
            property.refresh_from_db()
            property.on_sale = True
            property.save()

            return redirect(reverse('property-index'))
    else:
        return render(request, 'property/payment_review.html', {
            'property': get_object_or_404(Property, pk=id),
            'id': id
        })

def payment_successful(request):

    if request.method == 'GET':
        return render(request, 'property/payment_successful.html', dict())



