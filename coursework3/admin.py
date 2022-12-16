from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Items

admin.site.register(User, UserAdmin)
admin.site.register(Items)
class User(admin.ModelAdmin):
    list_display = ['email','password','date_of_birth','profile_image']
    list_editable = ['date_of_birth']