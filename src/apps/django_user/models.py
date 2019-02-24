from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from utils.choices import USER_ROLES
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
    )
    role = models.CharField(max_length=15, choices=USER_ROLES)
    # for admin site
    is_staff = models.BooleanField()

    objects = UserManager()

    USERNAME_FIELD = "email"
