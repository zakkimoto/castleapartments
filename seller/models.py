from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Seller(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.CharField(max_length=999, blank=True)
    email = models.CharField(max_length=200)
    agent = models.BooleanField()
    user = models.OneToOneField(User)

    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)

