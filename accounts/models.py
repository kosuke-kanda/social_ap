from django.db import models

from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager


class User(AbstractUser):
    pass

# class User(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=255, unique=True)
    # email = models.EmailField(max_length=255, unique=True)
    # password = models.CharField(max_length=20, verbose_name='パスワード' )

    # objects = UserManager()

    # USERNAME_FIELD = 'username' 
    # REQUIRED_FIELDS = [] 

    # class Meta:
    #     db_table = 'users' #テーブル名を指定