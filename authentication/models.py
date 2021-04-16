from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.validators import RegexValidator



class UserManager(BaseUserManager):


    def create_user(self, first_name, last_name, mobileNo, address, password=None):
        """Creates and saves a User with the given email, first name, last name
        and password."""

        if first_name is None:
            raise TypeError("Users should have a first_name")
        if last_name is None:
            raise TypeError("Users should have a last_name")
        if mobileNo is None:
            raise TypeError("Users must have a valid Mobile No.")
        if address is None:
            raise TypeError("Users must have a address")


        # user = self.model(username=username, email=self.normalize_email(email))
        user = self.model(first_name=first_name, last_name=last_name, mobileNo=mobileNo, address=address)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, first_name, last_name, mobileNo, address, password=None):
        """Creates and saves a User with the given email, first name, last name
        and password."""

        if first_name is None:
            raise TypeError("Users should have a first_name")
        if last_name is None:
            raise TypeError("Users should have a last_name")
        if mobileNo is None:
            raise TypeError("Users must have a valid Mobile No.")
        if address is None:
            raise TypeError("Users must have a address")

        user = self.create_user(first_name, last_name, mobileNo, address, password)
        user.is_superuser = True
        user.is_stuff = True
        user.is_admin = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser
    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin
    # id is provided by Django by default
    first_name = models.CharField(max_length=100, unique=True, db_index=True)
    last_name = models.CharField(max_length=150, unique=True, db_index=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+919999999999'. Up to 12 digits allowed.")
    mobileNo = models.CharField(validators=[phone_regex], max_length=13, unique=True) # validators should be a list
    address = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'mobileNo'
    REQUIRED_FIELDS = ['first_name', 'address']

    objects = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def tokens(self):
        return ''




