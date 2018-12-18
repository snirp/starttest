from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.conf import settings

# 'email' or 'username' or 'username_email'
auth = settings.ACCOUNT_AUTHENTICATION_METHOD

class UserManager(BaseUserManager):

  def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
    if auth != 'username' and not email:
        raise ValueError('Users must have an email address')
    if auth != 'email' and not username:
        raise ValueError('Users must have a username')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        username=username,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, username, password, **extra_fields):
    return self._create_user(email, username, password, False, False, **extra_fields)

  def create_superuser(self, email, username, password, **extra_fields):
    user=self._create_user(email, username, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    if auth != 'email':
        username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email' if auth == 'email' else 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/accounts/user/%i/" % (self.pk)

