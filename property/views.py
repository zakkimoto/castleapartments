from django.shortcuts import render, get_object_or_404, redirect

from property.forms.property_form import PropertyCreateForm
from property.models import Property, PropertyImage


def index(request):
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