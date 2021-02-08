from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Account, Stocks


# __________________________________ACCOUNT FUNCTIONALITY______________________________________________
# Login functionality
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "shares/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "shares/login.html")


# Logout functionality
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Register functionality
def register(request):
    if request.method == "POST":

        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        if email is None or password is None or first_name is None or last_name is None:
            return render(request, "network/register.html", {
                "message": "Please fill in all fields."
            })

        if password != confirmation:
            return render(request, "shares/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = get_user_model().objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "shares/register.html")


# __________________________________HTML PAGES______________________________________________
# Home page
def index(request):
    return render(request, "shares/index.html")


# Stock page
@login_required
def stocks(request):
    stocks_queryset = Stocks.objects.all()
    return render(request, "shares/stocks.html", {
        "stocks": stocks_queryset
    })


# News page
@login_required
def news(request):
    return render(request, "shares/news.html")


# Stockinfo page
@login_required
def stockinfo(request):
    return render(request, "shares/stockinfo.html")


# ______________________________________ API's ___________________________________________________
# news API
@login_required
def getnews(request):
    return None


# stockinfo API
def getstockinfo(request):
    return None
