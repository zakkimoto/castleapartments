from django.shortcuts import render
from property.models import Property


def index(request):
    context = {'properties': Property.objects.all().order_by('streetname')}
    return render(request, 'property/index.html', context)