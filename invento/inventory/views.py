from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import get_collection

from . import forms


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
