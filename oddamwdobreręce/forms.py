from django.forms import ModelForm
from .models import User


class UserCreationForm(ModelForm):
    # form to create new user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
