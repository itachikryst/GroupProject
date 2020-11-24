from django.db import models

# Create your models here.

class Workshop(models.Model):
    USERNAME = models.CharField(max_length=16, null=False)
    PASSWORD = models.CharField(max_length=64, null=False)
    NAME = models.TextField(null=False)
    EMAIL = models.EmailField(null=False)
    PHONENUMBER = models.CharField(max_length=9, null=False)
    WORKERS = []
    MANAGER = []
    OWNER = []