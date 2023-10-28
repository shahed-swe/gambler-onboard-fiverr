from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from solo.models import SingletonModel


class InternalData(SingletonModel):
    class Meta:
        verbose_name = _('Internal data')
        verbose_name_plural = _('Internal data')

    id = models.AutoField(primary_key=True)
    maintenance_mode = models.BooleanField(default=False)
    last_livestream = models.DateTimeField(auto_now_add=True)


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = ['id']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    last_seen = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def get_username(self):
        return self.username

    def is_super_admin_user(self):
        return self.is_superuser

    def is_admin_user(self):
        return self.is_admin

    def is_staff_user(self):
        return self.is_staff
