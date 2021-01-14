from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from client.models import User
from .forms import RegistrationForm



def homepageView(request, *args, **kwargs):
    context = {}
    return render(request, "index.html", context)


def loginPageView(request, *args, **kwargs):
    logout(request)
    if request.POST:
        print("test1")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("test")
            return redirect("home")

    else:
        print("test2")
        form = AuthenticationForm()
    print("test3")
    context = {'form': form}
    return render(request, "login.html", context)


def registerPageView(request, *args, **kwargs):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:

            context["registration_form"] = form
    else:

        form = RegistrationForm()
        context["registration_form"] = form


    return render(request, "register.html", context)


def managerOrdersView(request, *args, **kwargs):
    context = {}
    return render(request, "manager-orders.html", context)


def userOrdersView(request, *args, **kwargs):
    context = {}
    return render(request, "user-orders.html", context)


def userSearchView(request, *args, **kwargs):
    context = {}
    return render(request, "user-search.html", context)


def workerOrdersView(request, *args, **kwargs):
    context = {}
    return render(request, "worker-orders.html", context)
