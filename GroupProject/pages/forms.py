from django.contrib.auth.forms import UserCreationForm
from django import forms
from client.models import User
from django.forms import ModelForm
from workshop.models import Order

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("type", "username", "first_name", "last_name", "email",
                  "password1", "password2")


class OrderStatusForm(ModelForm):
    class Meta:
        model = Order
        fields = ['STATUS']
