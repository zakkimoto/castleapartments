from django.db import models
from seller.models import Seller
# Create your models here.

class PropertyType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Property(models.Model):
    streetname = models.CharField(max_length=225)
    description = models.CharField(max_length=999, blank=True)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    address = models.CharField(max_length=225)
    postal_code = models.CharField(max_length=200)
    city = models.CharField(max_length=225)
    country = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    size = models.FloatField()
    price = models.FloatField()
    on_sale = models.BooleanField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    def __str__(self):
        return self.streetname

class PropertyImage(models.Model):
    image = models.CharField(max_length=999)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    def __str__(self):
        return self.image