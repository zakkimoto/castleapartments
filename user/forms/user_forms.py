from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django.forms import ModelForm, widgets


class SignUpForm(UserCreationForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}))
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email','id')

class UserUpdateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        exclude = [ 'id' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control' }),
            'last_name': widgets.TextInput(attrs={'class': 'form-control' }),
            'email': widgets.TextInput(attrs={'class': 'form-control' }),
            'username': widgets.TextInput(attrs={'class': 'form-control' }),
            'password': widgets.TextInput(attrs={'class': 'form-control' })
        }