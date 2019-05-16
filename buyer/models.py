from django.db import models


class CreditCard(models.Model):
    credit_card = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=5)
    cvc = models.IntegerField()


# Create your models here.
class Buyer(models.Model):
    buyer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    ssc = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    credit_card = models.OneToOneField(CreditCard, on_delete=models.CASCADE, null=True)
    #new_property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.buyer_name

class BuyerSession(models.Model):
    session = models.CharField(max_length=200)
    search_term = models.CharField(max_length=200)
    #buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.search_term