from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from . import models

from . import forms


def index(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            organization = form.cleaned_data["organization"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["confirmPassword"]
            if password != confirm:
                return render(
                    request,
                    "inventory/index.html",
                    {"form": forms.SignUpForm, "warning": "please check all fields"},
                )
            return HttpResponse(username + email + organization + password)
    data = models.get_collection("Inventories")
    return render(request, "inventory/index.html", {"form": forms.SignUpForm})
