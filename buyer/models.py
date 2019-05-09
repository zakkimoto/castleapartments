from django.db import models
from property.models import Property

# Create your models here.
class Buyer(models.Model):
    buyer_name = models.CharField(max_length=200)
    streetname = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    ssc = models.CharField(max_length=10)
    credit_card = models.CharField(max_length=16)
    email = models.CharField(max_length=200)
    new_property = models.ForeignKey(Property, on_delete=models.CASCADE)

