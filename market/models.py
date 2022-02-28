from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    user_cell_phone = models.CharField(max_length=50, default='', null=True, blank=True)


class Produce(models.Model):
    produce_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=200)
    qty = models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.produce_name