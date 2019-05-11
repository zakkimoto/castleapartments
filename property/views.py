from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from property.forms.property_form import PropertyCreateForm, PropertyUpdateForm
from property.models import Property, PropertyImage


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        properties = [{
            'id': x.id,
            'streetname': x.streetname,
            'description': x.description,
            'firstImage': x.propertyimage_set.first().image
        } for x in Property.objects.filter(streetname__icontains=search_filter)]
        return JsonResponse({ 'data': properties })
    context = {'properties': Property.objects.all().order_by('streetname')}
    return render(request, 'property/index.html', context)

def get_property_by_id(request, id):
    return render(request, 'property/property_details.html', {
        'property': get_object_or_404(Property, pk=id)
    })

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

def delete_property(request, id):
    property = get_object_or_404(Property, pk=id)
    property.delete()
    return redirect('property-index')

def update_property(request, id):
    instance = get_object_or_404(Property, pk=id)
    if request.method == "POST":
        form = PropertyUpdateForm( data= request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('property_details', id=id)
    else:
        form = PropertyUpdateForm(instance=instance)
    return render(request, 'property/update_property.html', {
        'form': form,
        'id' : id
    })
