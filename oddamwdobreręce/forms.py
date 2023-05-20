from django.forms import ModelForm
from django import forms
from .models import User


class UserCreationForm(ModelForm):
    # form to create new user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]


class LoginForm(forms.Form):
    email = forms.CharField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
