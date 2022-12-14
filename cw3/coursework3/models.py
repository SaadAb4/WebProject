from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from datetime import datetime

class CustomUserManager(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("no valid email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email,password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    date_of_birth = models.DateField(blank=True, default='2001-01-01')
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Items(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    startingPrice = models.DecimalField(max_digits=5, decimal_places=2)
    auctionEnd = models.DateTimeField(default='2022-12-12')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'startingPrice': self.startingPrice,
            'auctionEnd': self.auctionEnd, 
        }