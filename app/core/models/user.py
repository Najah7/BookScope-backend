"""
User Model
"""

import uuid
import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password) # encrypts the password
        user.save(using=self._db) # standard procedure for saving objects in django
        return user
    
    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True # automatically created by PermissionsMixin
        user.is_superuser = True # automatically created by PermissionsMixin
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    school_id = models.CharField(max_length=255, unique=True)
    major_id = models.CharField(max_length=255, unique=True)
    rank_id = models.CharField(max_length=255, unique=True)
    role_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=False) # unique=True is a validator
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null=False, blank=False)
    self_introduction = models.TextField(max_length=1000, blank=True, null=True)
    icon = models.ImageField(upload_to="user_icon", blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True) # automatically created by PermissionsMixin
    is_staff = models.BooleanField(default=False) # automatically created by PermissionsMixin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email" # defines the field to use for logging in
    # REQUIRED_FIELDS = [] # defines the required fields for creating a user
    
    def __str__(self):
        return f"name: {self.user_name} email: {self.email}"

