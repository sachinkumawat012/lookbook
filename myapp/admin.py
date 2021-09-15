from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Profile
# Register your models here.
@admin.register(Profile)
class Profiles(admin.ModelAdmin):
    display_list = ['image', 'caption']