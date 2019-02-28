from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from utils.choices import USER_ROLES
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True, null=True
    )
    name = models.CharField(max_length=500)
    role = models.CharField(max_length=15, choices=USER_ROLES)
    USERNAME_FIELD = "email"

    # for admin setting
    is_staff = models.BooleanField()
    REQUIRED_FIELDS = ["name"]
    objects = UserManager()
