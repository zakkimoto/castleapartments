from django.contrib.auth.models import User
from django.db import models

# Create eayour models here.
class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        user = User.objects.filter(id=self.user_id).values()
        return f'{user[0]["first_name"]} {user[0]["last_name"]}'


