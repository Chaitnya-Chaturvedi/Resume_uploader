


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


STATE_CHOICES = (
    ("MP","MP"),
    ("GUJRAT","GUJRAT"),
    ("MH","MH"),
    ("UP","UP"),
    ("DELHI","DELHI"),
    ("KARNATAKA","KARNATAKA"),
    ("KERALA","KERALA"),

)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to= "profileimg", blank=True)
    my_file = models.FileField(upload_to= "doc", blank=True)
