from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class loginForm(forms.Form):
    CHOICES = (('Klient', 'Klient'), ('Pracownik', 'Pracownik'),('Kierownik', 'Kierownik'),('Warsztat', 'Warsztat'),('Admin', 'Admin'))
    accountType = forms.ChoiceField(choices=CHOICES)
    email = forms.CharField()
    password = forms.CharField()


class registerForm(forms.Form):
    CHOICES = (('Klient', 'Klient'), ('Pracownik', 'Pracownik'),('Kierownik', 'Kierownik'),('Warsztat', 'Warsztat'),('Admin', 'Admin'))
    accountType = forms.ChoiceField(choices=CHOICES)
    userName = forms.CharField()
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

