from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Items, Questions

admin.site.register(User, UserAdmin)
admin.site.register(Items)
admin.site.register(Questions)
class User(admin.ModelAdmin):
    list_display = ['email','password','date_of_birth','profile_image']
    list_editable = ['date_of_birth']