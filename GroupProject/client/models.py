from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        KLIENT = "Klient"
        PRACOWNIK = "Pracownik"
        KIEROWNIK = "Kierownik"
        WARSZTAT = "Warsztat"

    type = models.CharField(_("Type"), max_length=50,
                            choices=Types.choices, default=Types.KLIENT)

    # name = models.CharField(_("Name of User"), blank=True, max_length=255)
    # username = models.CharField(_("Username of a User"), blank=True,
    #                             max_length=255)
    # password = models.CharField(_("Password of a User"), blank=True,
    #                             max_length=255)
    # email = models.CharField(_("Username of a User"), blank=True,
    #                             max_length=255)
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class KlientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            type=User.Types.KLIENT)


class PracownikManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            type=User.Types.PRACOWNIK)


class KierownikManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            type=User.Types.KIEROWNIK)


class WarsztatManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            type=User.Types.WARSZTAT)


# class KlientMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # POLA
#
#
# class PracownikMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # POLA
#
#
# class KierownikMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # POLA
#
#
# class WarsztatMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # POLA


class Klient(User):
    objects = KlientManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.KLIENT
        return super().save(*args, **kwargs)


class Pracownik(User):
    objects = PracownikManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PRACOWNIK
        return super().save(*args, **kwargs)


class Kierownik(User):
    objects = KierownikManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.KIEROWNIK
        return super().save(*args, **kwargs)


class Warsztat(User):
    objects = WarsztatManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.WARSZTAT
        return super().save(*args, **kwargs)
