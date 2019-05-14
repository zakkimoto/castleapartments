from django.shortcuts import get_object_or_404, redirect, render
from buyer.models import Buyer, PaymentBuyer
from property.forms.property_form import PropertyBuyForm, PropertyPaymentForm


def buy_property(request, id):
    instance = get_object_or_404(Buyer, pk=id)
    if request.method == "POST":
        form = PropertyBuyForm(data = request.POST, instance=instance)
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
        'review': get_object_or_404(Buyer, pk=id)
    })
