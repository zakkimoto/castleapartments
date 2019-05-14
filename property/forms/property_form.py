from django.forms import ModelForm, widgets
from django import forms

from property.models import Property
from buyer.models import Buyer, PaymentBuyer

class PropertyUpdateForm(ModelForm):
    class Meta:
        model = Property
        exclude = [ 'id' ]
        widgets = {
            'streetname': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'type': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'bedrooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'form-control'}),
            'seller': widgets.Select(attrs={'class': 'form-control'})
        }

class PropertyCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}))
    image2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}))
    image3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}))
    image4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}))
    class Meta:
        model = Property
        exclude = [ 'id' ]
        widgets = {
            'streetname': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Streetname'}),
            'description': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe your property well, try to sell it!'}),
            'type': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal code'}),
            'city': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'country': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'bedrooms': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder':'How many bedrooms are in the property?'}),
            'bathrooms': widgets.NumberInput(attrs={'class': 'form-control','placeholder':'How many bathrooms are in the property?'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder':'How big is the property in sqm?'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'seller': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'form-control'}),
        }



class PropertyPaymentForm(ModelForm):
    class Meta:
        model = PaymentBuyer
        exclude = ['email']
        widgets = {
            'credit_card': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Credit Card Number.'}),
            'exp_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'csv': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'3 digit number on back of card.'}),
        }

class PropertyBuyForm(ModelForm):
    class Meta:
        model = Buyer
        exclude = ['id']
        widgets = {
            'buyer_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your full name.'}),
            'address': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your current streetname.'}),
            'city': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your current city.'}),
            'country': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your current country of living.'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your current postal code.'}),
            'ssc': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your social security number.'}),
            'email': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Type in your email.'}),
            'new_property': widgets.Select(attrs={'class': 'form-control'})
        }
