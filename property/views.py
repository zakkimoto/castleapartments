from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect

from buyer.models import PaymentBuyer, Buyer
from property.forms.property_form import PropertyCreateForm, PropertyUpdateForm, PropertyBuyForm, PropertyPaymentForm
from property.models import Property, PropertyImage


# def index(request):
#    if 'search_filter' in request.GET:
#        search_filter = request.GET['search_filter']
#        properties = [{
#            'id': x.id,
#            'streetname': x.streetname,
#            'description': x.description,
#            'firstImage': x.propertyimage_set.first().image,
#            'country': x.country,
#            'size': x.size,
#        } for x in Property.objects.filter(streetname__contains=search_filter)]
#        return JsonResponse({'data': properties})
#    context = {'properties': Property.objects.all().order_by('streetname')}
#    return render(request, 'property/index.html', context)

def _search_properties(search_term):
    return Property.objects.annotate(
        search=SearchVector('streetname', 'description', 'address', 'country')
    ).all().filter(search=search_term, on_sale=True).order_by('streetname')


def filter(request):
    print('in filter')
    if request.method == 'GET':

        print('in filter GET')
        bedrooms = request.GET.get('bedrooms', '')
        city = request.GET.get('city', '')
        postal_code = request.GET.get('postal_code', '')

        print('in filter GET after parameters')
        print('bedrooms = ', bedrooms)
        print('city = ', city)
        print('postal_code = ', postal_code)

        query = Q(on_sale=True)
        if postal_code:
            query &= Q(postal_code=postal_code)
        if bedrooms:
            query &= Q(bedrooms=bedrooms)
        if city:
            query &= Q(city=city)

        print('query = ', query)

        properties = Property.objects.filter(query)

        context = {'properties': properties}
        print('in filter GET after QUERY')
        return render(request, 'property/index.html', context)
    else:
        return HttpResponseNotAllowed()


def search(request):
    if request.method == 'GET':
        if 'search_filter' in request.GET:
            search_filter = request.GET['search_filter']
            properties = [{
                'id': x.id,
                'streetname': x.streetname,
                'description': x.description,
                'firstImage': x.propertyimage_set.first().image,
                'country': x.country,
                'size': x.size,
            } for x in _search_properties(search_filter)]
            return JsonResponse({'data': properties})
    else:
        return HttpResponseNotAllowed()


def index(request):
    if request.method == 'GET':
        if 'search' in request.GET:
            search_term = request.GET['search']
            print('here')
            properties = _search_properties(search_term)
        else:
            properties = Property.objects.filter(on_sale=True).order_by('streetname')

        context = {'properties': properties}
        return render(request, 'property/index.html', context)
    else:
        return HttpResponseNotAllowed()


# @login_required
def get_property_by_id(request, id):
    return render(request, 'property/property_details.html', {
        'property': get_object_or_404(Property, pk=id)
    })


# @login_required
def create_property(request):
    if request.method == 'POST':
        form = PropertyCreateForm(data=request.POST)
        if form.is_valid():
            property = form.save()
            property_image = PropertyImage(image=request.POST['image'], property=property)
            property_image.save()
            property_image2 = PropertyImage(image=request.POST['image2'], property=property)
            property_image2.save()
            return redirect('property-index')
    else:
        form = PropertyCreateForm()
    return render(request, 'property/create_property.html', {
        'form': form
    })


# @login_required
def delete_property(request, id):
    property = get_object_or_404(Property, pk=id)
    property.delete()
    return redirect('property-index')


# @login_required
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
    instance = get_object_or_404(Buyer, pk=id)
    if request.method == "POST":
        form = PropertyBuyForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_property', id=id)
    else:
        form = PropertyBuyForm(instance=instance)
    return render(request, 'property/buy_property.html', {
        'form': form,
        'id': id
    })

def payment_property(request, id):
    instance = get_object_or_404(PaymentBuyer, pk=id)
    if request.method == "POST":
        form = PropertyPaymentForm(data = request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('payment_review', id=id)
    else:
        form = PropertyPaymentForm(instance=instance)
    return render(request, 'property/payment_property.html', {
        'form': form,
        'id': id
    })

def payment_review(request, id):
    return render(request, 'property/payment_review.html', {
        'review': get_object_or_404(pk=id)
    })
