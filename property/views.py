from django.shortcuts import render, get_object_or_404
from property.models import Property


def index(request):
    context = {'properties': Property.objects.all().order_by('streetname')}
    return render(request, 'property/index.html', context)

def get_property_by_id(request, id):
    return render(request, 'property/property_details.html', {
        'property': get_object_or_404(Property, pk=id)
    })