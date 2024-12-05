from bson.objectid import ObjectId
from django.core.exceptions import ValidationError
from django.core.serializers.base import models
from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.

from .models import get_collection

from . import forms

from .utilities import sha256

global userData


def index(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            users = get_collection("Users")
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            organization = form.cleaned_data["organization"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["confirmPassword"]

            if users.find_one({"username": username}) != None:
                return render(
                    request,
                    "inventory/index.html",
                    {
                        "form": forms.SignUpForm(request.POST),
                        "warning": "please choose another username",
                    },
                )
            if password != confirm:
                return render(
                    request,
                    "inventory/index.html",
                    {
                        "form": forms.SignUpForm(request.POST),
                        "warning": "please check all fields",
                    },
                )

            userData = {
                "username": username,
                "email": email,
                "organization": organization,
                "password": sha256(password),
                "ownedInventories": [],
            }

            users.insert_one(userData)
            # make this path to login
            return login(None)
        else:
            return render(
                request,
                "inventory/index.html",
                {
                    "form": forms.SignUpForm(request.POST),
                    "warning": "please check all fields",
                },
            )
    return render(request, "inventory/index.html", {"form": forms.SignUpForm})


def login(request):
    form = forms.loginForm()
    if request.method == "POST":
        users = get_collection("Users")
        form = forms.loginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            # hash the password
            password = form.cleaned_data["password"]

            user = users.find_one({"username": username, "password": sha256(password)})

            if user:
                # return here the dashboard
                global userData
                userData = user
                return userDashboard(request)

        return render(
            request,
            "inventory/login.html",
            {"form": form, "warning": "Invalid credentials"},
        )
    return render(
        request, "inventory/login.html", {"form": form, "warning": "no warning"}
    )


def userDashboard(request):
    global userData
    inventoriesDB = get_collection("Inventories")
    arr = list(userData["ownedInventories"])

    inventoriesOwned = dict()

    for inventoryId in arr:
        inventoriesOwned[inventoryId] = inventoriesDB.find_one({"_id": inventoryId})

    sharedInventoryIds = inventoriesDB.find({"sharedTo": userData["username"]})

    return render(
        request,
        "inventory/userDashboard.html",
        {
            "userData": userData,
            "inventoriesOwned": inventoriesOwned,
            "sharedInventories": sharedInventoryIds,
        },
    )
