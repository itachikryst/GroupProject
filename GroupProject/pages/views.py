from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import loginForm
from .forms import registerForm



def homepage_view(request, *args, **kwargs):
    return render(request, "index.html")

def loginPage(request):
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, "login.html",context)

def registerPage(request):
    registerForms = registerForm()
    if request.method == 'POST':
        registerForms = loginForm(request.POST)
        if registerForms.is_valid():
            registerForms.save()
    context = {'form': registerForms}
    return render(request, "register.html",context)
