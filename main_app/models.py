from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from main_app.manager import UserAccountManager


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email address',
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(
        max_length=30,
        verbose_name='first name',
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='last name',
    )
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
