from django.db import models

# Create your models here.

class PropertyType(models.Model):
    name = models.CharField(max_length=255)

class Property(models.Model):
    streetname = models.CharField(max_length=225)
    description = models.CharField(max_length=999, blank=True)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    address = models.CharField(max_length=225)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    size = models.FloatField()
    price = models.FloatField()
    on_sale = models.BooleanField()
    seller = models.ForeignKey() # TODO: Map to seller

class PropertyImage(models.Model):
    image = models.CharField(max_length=999)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)