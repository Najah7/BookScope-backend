"""
User Model
"""

import os

from django.conf import settings
from django.db import models as DjangoModels
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from core import models as CoreModels


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)  # encrypts the password
        user.save(using=self._db)  # standard procedure for saving objects in django
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True  # automatically created by PermissionsMixin
        user.is_superuser = True  # automatically created by PermissionsMixin
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    class Meta:
        db_table = "user"
        app_label = "core"

    # NOTE: Userから参照することが多いので、User側で定義した（個人的に参照をよくする方で明示したほうがいいと思う。）
    post_like = DjangoModels.ManyToManyField(
        CoreModels.PostLike, related_name="post_like", blank=True
    )
    post_comment = DjangoModels.ManyToManyField(
        CoreModels.PostComment, related_name="post_comment", blank=True
    )

    # フィールド
    email = DjangoModels.EmailField(
        max_length=255, unique=True, null=False
    )  # unique=True is a validator
    user_name = DjangoModels.CharField(max_length=255, default="no user name")
    password = DjangoModels.CharField(max_length=255, null=False, blank=False)
    self_introduction = DjangoModels.TextField(max_length=1000, blank=True, null=True)
    icon = DjangoModels.ImageField(upload_to="user_icon", blank=True, null=True)
    twitter = DjangoModels.URLField(blank=True, null=True)
    instagram = DjangoModels.URLField(blank=True, null=True)
    facebook = DjangoModels.URLField(blank=True, null=True)
    linkedin = DjangoModels.URLField(blank=True, null=True)
    is_active = DjangoModels.BooleanField(
        default=True
    )  # automatically created by PermissionsMixin
    is_staff = DjangoModels.BooleanField(
        default=False
    )  # automatically created by PermissionsMixin
    created_at = DjangoModels.DateTimeField(auto_now_add=True)
    updated_at = DjangoModels.DateTimeField(auto_now=True)

    # モデルマネージャー
    objects = UserManager()

    USERNAME_FIELD = "email"  # defines the field to use for logging in
    # REQUIRED_FIELDS = [] # defines the required fields for creating a user

    def __str__(self):
        return f"name: {self.user_name} email: {self.email}"
