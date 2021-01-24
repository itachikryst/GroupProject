from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from client.models import User, Klient
from workshop.models import Order, Workshop
from .forms import RegistrationForm



def homepageView(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {"user": request.user, "userType": request.user.type}
        # u = User.objects.filter(email=request.user.email)
        # print(u.__class__)
        # u.__class__ = Klient
        # u.save()
        # print(User.objects.all)
    else:
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
            if user.type == "Pracownik":
                return redirect("workerorders")
            if user.type == "Kierownik":
                return redirect("managerorders")
            if user.type == "Użytkownik":
                return redirect("usersearch")
            else:
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
    if request.user.is_authenticated:
        orders = list(Order.objects.all())
        for id, order in enumerate(orders):
            orders[id] = (order, id)
        # print(orders)
        context = {"user": request.user, "userType": request.user.type,
                   "orders": orders}
    else:
        context = {}
    return render(request, "manager-orders.html", context)


def userOrdersView(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {"user": request.user, "userType": request.user.type}
    else:
        context = {}
    return render(request, "user-orders.html", context)


def userSearchView(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {"user": request.user, "userType": request.user.type}
    else:
        context = {}
    return render(request, "user-search.html", context)


def workerOrdersView(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {"user": request.user, "userType": request.user.type}
    else:
        context = {}
    return render(request, "worker-orders.html", context)
