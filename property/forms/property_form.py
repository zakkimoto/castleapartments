from django.forms import ModelForm, widgets
from django import forms
from property.models import Property


class PropertyCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}))
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
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
        }