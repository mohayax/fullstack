from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class userAccountManager(BaseUserManager):
    def create_user(self, name, email,password = None ):
        if not email:
            raise ValueError('email must be provided!')
        
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user




class userAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = userAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
