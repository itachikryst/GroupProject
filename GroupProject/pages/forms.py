from django.contrib.auth.forms import UserCreationForm
from django import forms
from client.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("type", "username", "first_name", "last_name", "email",
                  "password1", "password2")
