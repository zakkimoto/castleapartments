from django.forms import ModelForm, widgets
from django import forms
from property.models import Property


class PropertyCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
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
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'seller': widgets.Select(attrs={'class': 'form-control'})
        }