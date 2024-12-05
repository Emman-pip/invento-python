from django import forms
from django.forms import widgets


def fieldStyle():
    return "height: 1.5rem; padding: .5rem; border-radius: 100px"


class SignUpForm(forms.Form):
    # widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "username",
            }
        ),
    )
    email = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "email",
            }
        ),
    )
    organization = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "organization",
            }
        ),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password",
            }
        ),
    )
    confirmPassword = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "confirm password",
            }
        ),
    )
