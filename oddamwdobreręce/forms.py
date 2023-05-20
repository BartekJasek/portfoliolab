from django.forms import ModelForm
from django import forms
from .models import User


class UserCreationForm(ModelForm):
    # form to create new user
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.CharField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
