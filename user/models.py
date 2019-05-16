from django.contrib.auth.models import User
from django.db import models

class UserImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
