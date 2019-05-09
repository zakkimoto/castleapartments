from django.shortcuts import render

# Create your views here.
from seller.models import Seller


def index(request):
    return render(request, 'seller/index.html', {
        'sellers': Seller.objects.all()
    })