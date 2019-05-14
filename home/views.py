from django.shortcuts import render
from django.http import JsonResponse
from property.models import Property

# Create your views here.



def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        properties = [{
            'id': x.id,
            'streetname': x.streetname,
            'description': x.description,
            'firstImage': x.propertyimage_set.first().image,
            'country': x.country,
            'size': x.size,
        } for x in Property.objects.filter(streetname__contains=search_filter)]
        return JsonResponse({'data': properties})
    context = {'properties': Property.objects.all().order_by('streetname')}
    return render(request, 'home/index.html', context)

