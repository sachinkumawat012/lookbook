from django import forms
from django.db import models
from .models import UserPostModel


class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPostModel
        fields = ["image", "description"]