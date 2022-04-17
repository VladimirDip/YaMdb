from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    USER = 'user', _('User')
    MODERATOR = 'moderator', _('Moderator')
    ADMIN = 'admin', _('Admin')


class User(AbstractUser):
    email = models.EmailField(_('email addres'), unique=True)
    bio = models.TextField(max_length=300, blank=True)
    confirmation_code = models.CharField(max_length=60, blank=True)
    description = models.TextField(max_length=300, blank=True)
    role = models.CharField(
        max_length=25, choices=Role.choices, default=Role.USER
    )

    @property
    def is_admin(self):
        return self.role == Role.ADMIN or self.is_staff

    @property
    def is_moderator(self):
        return self.role == Role.MODERATOR

