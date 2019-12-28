from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_service = models.BooleanField(null=True, blank=True, default=False)
    is_customer = models.BooleanField(null=True, blank=True, default=False)
    mobile = models.BigIntegerField()

class Cregister(models.Model):
    pass


class Account(models.Model):
    pass
