from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email", max_length=100, unique=True, error_messages={ "unique": "A user with that email already exists" })
    username = models.CharField("username", max_length=50, unique=True, error_messages={ "unique": "That username already exists" })
    name = models.CharField("name", max_length=100)
    lastname = models.CharField("lastname", max_length=100)

    is_editor = models.BooleanField("is_editor", default=False)
    is_staff = models.BooleanField("is_staff", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.name + ' ' + self.lastname