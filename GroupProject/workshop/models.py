# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _


class Workshop(models.Model):
    NAME = models.CharField(max_length=16, null=False, default="Warsztat")
    LOCALIZATION = models.CharField(max_length=16, null=False)


class Order(models.Model):
    class Status(models.TextChoices):
        DOWZIECIA = "Do wziecia"
        ZLECONE = "Zlecone"
        WTRAKCIE = "W trakcie"
        GOTOWE = "GOTOWE"

    STATUS = models.CharField(_("Type"), max_length=50,
                              choices=Status.choices, default=Status.DOWZIECIA)
    CLIENTMAILADDRESS = models.CharField(max_length=64, null=True)
    NAME = models.CharField(max_length=32, null=False)
    DESC = models.CharField(max_length=512, null=False)
    WORKSHOP = models.ForeignKey(Workshop, on_delete=models.PROTECT, null=True)
