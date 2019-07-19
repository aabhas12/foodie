from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
        Parent model
    """
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True


class Users(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
        Defining Users
    """
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    firstname = models.CharField(_('first name'), max_length=30)
    lastname = models.CharField(_('last name'), max_length=30)
    avatar = models.URLField(null=True, blank=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    sms = models.CharField(max_length=12, blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
        db_table = 'user'
