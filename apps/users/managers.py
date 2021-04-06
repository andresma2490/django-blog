from django.db import models
from django.contrib.auth.models import UserManager

class UserManager(UserManager, models.Manager):
    def _create_user(self, username, email, password, **extra_fields):
        return super(UserManager, self)._create_user(username, email, password, **extra_fields)

    def create_user(self, username, email, password, **extra_fields):
        return super(UserManager, self).create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return super(UserManager, self).create_superuser(username, email, password, **extra_fields)
