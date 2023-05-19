from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserCreationForm(ModelForm):
    # form to create new user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]


class LoginForm(AuthenticationForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
