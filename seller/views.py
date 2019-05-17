from seller.models import Seller
from django.shortcuts import render, get_object_or_404, redirect
from seller.forms.seller_form import SellerUpdateForm


def index(request):
    sellers = Seller.objects.all().values("user__first_name", "user__last_name",
                                          "user__email", "user__userimage__image", "id")
    return render(request, 'seller/index.html', {
        'sellers': sellers
    })


def get_seller_by_id(request, id):
    return render(request, 'seller/seller_details.html', {
        'seller': get_object_or_404(Seller, pk=id)
    })


def update_seller(request, id):
    instance = get_object_or_404(Seller, pk=id)
    if request.method == 'POST':
        form = SellerUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('seller_details', id=id)
    else:
        form = SellerUpdateForm(instance=instance)
    return render(request, 'seller/update_seller.html', {
        'form': form,
        'id': id
    })
