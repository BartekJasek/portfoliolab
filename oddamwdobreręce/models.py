from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from localflavor.pl.forms import PLPostalCodeField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.TextField


class Institution(models.Model):
    INSTITUTION = (
        ("fundacja", "fundacja"),
        ("organizacja pozarządowa", "organizacja pozarządowa"),
        ("zbiórka lokalna", "zbiórka lokalna"),
    )
    name = models.TextField
    description = models.TextField
    subject = models.TextField(choices=INSTITUTION)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    city = models.TextField
    zip_code = PLPostalCodeField()
    pick_up_date = models.DateField
    pick_up_time = models.TimeField
    pick_up_comment = models.TextField
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
