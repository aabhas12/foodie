from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class Users(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, null=True)
    password = models.CharField(_('password'), max_length=128, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    facebook_id = models.CharField(null=True, max_length=30)
    google_id = models.CharField(null=True, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)