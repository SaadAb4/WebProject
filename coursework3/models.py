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
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #date_of_birth = models.DateField(null=True, blank=True)
    test = models.BooleanField(default=True)
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self) -> str:
        return str(self.date_of_birth)
    def __str__(self) -> str:
        return str(self.email)
    def __str__(self) -> str:
        return str(self.profile_image)
    

    def to_dict(self):
        return {
            'id': self.id,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'profile_image': self.profile_image,
        }

class Items(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=50, default='')
    startingPrice = models.DecimalField(max_digits=5, decimal_places=2)
    auctionEnd = models.DateTimeField(null=True,blank=True)
    item_pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'startingPrice': self.startingPrice,
            'auctionEnd': self.auctionEnd,
            'item_pic' : self.item_pic,
        }