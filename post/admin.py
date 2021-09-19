from django.contrib import admin
from .models import UserPostModel

# Register your models here.

@admin.register(UserPostModel)
class UserPostAdmin(admin.ModelAdmin):
    display_list = ['image', 'description']
