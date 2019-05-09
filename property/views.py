from django.shortcuts import render

properties = [
    {
        'streetname': 'Karsnesbraut',
        'price': 28.5
    },
    {
        'streetname': 'Asendi',
        'price': 40
    }
]


# Create your views here.
def index(request):
    context = {'properties': properties}
    return render(request, 'Property/index.html', context)