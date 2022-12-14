from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Items

admin.site.register(User, UserAdmin)
class User(admin.ModelAdmin):
    fields = ['email','password','date_of_birth','profile_image']