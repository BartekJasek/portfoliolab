from phonenumber_field.modelfields import PhoneNumberField
from localflavor.pl.forms import PLPostalCodeField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.TextField()


class Institution(models.Model):
    INSTITUTION = (
        ("fundacja", "fundacja"),
        ("organizacja pozarządowa", "organizacja pozarządowa"),
        ("zbiórka lokalna", "zbiórka lokalna"),
    )
    name = models.TextField()
    description = models.TextField()
    subject = models.TextField(choices=INSTITUTION)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    city = models.TextField()
    zip_code = PLPostalCodeField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
