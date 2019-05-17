
from django.shortcuts import render, redirect

from seller.models import Seller
from user.forms.user_forms import SignUpForm
from user.models import UserImage


def register(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_image = UserImage(image=request.POST['image'])
            user_image.user_id = user.id
            user_image.save()

            seller = Seller()
            seller.user = user
            seller.save()

            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'user/register.html', {
        'form': form
    })

