from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Gremio
from django.db import IntegrityError

## Enpoint login
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "user/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "user/login.html")


## Logout view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

## Register view
def register(request):
    gremios = Gremio.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        gremio = Gremio.objects.get(id = int(request.POST["gremio"]))
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "user/register.html", {
                "message": "Passwords must match.",
                "gremios" : gremios
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.gremio = gremio
            user.save()
        except IntegrityError:
            return render(request, "user/register.html", {
                "message": "Username already taken.",
                "gremios" : gremios
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "user/register.html", {
            "gremios" : gremios
        })


'''
Endpoint para renderizar el index page
'''
def index(request):
    return render(request, "page/index.html")