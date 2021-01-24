# Create your models here.
from django.db import models

class Workshop(models.Model):
    NAME = models.CharField(max_length=16, null=False, default="Warsztat")
    LOCALIZATION = models.CharField(max_length=16, null=False)

    # USERNAME = models.CharField(max_length=16, null=False)
    # PASSWORD = models.CharField(max_length=64, null=False)
    # NAME = models.TextField(null=False)
    # EMAIL = models.EmailField(null=False)
    # PHONENUMBER = models.CharField(max_length=9, null=False)

class Order(models.Model):
    NAME = models.CharField(max_length=32, null=False)
    DESC = models.CharField(max_length=512, null=False)
    WORKSHOP = models.ForeignKey(Workshop, on_delete=models.PROTECT, null=True)