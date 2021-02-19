from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManage,PermissionMixin

class UserManager(BaseUserManage):
    def create_user(self,username,email,password=None):

        if username is None:
            raise TypeError("Username should not be empty.")
        if email is None:
            raise TypeError("Email should not be empty.")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()

    def create_superuser(self,username,email,password=None):

        if password is None:
            raise TypeError("Password should not be empty.")
       
        user=self.create_user(self,username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
        

class User(AbstractBaseUser,PermissionMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.Boolean(default=False)
    is_active=models.Boolean(default=False)
    is_staff=models.Boolean(default=False)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()

    def __str__(self):
        return self.username

    def token(self):
        return ""
