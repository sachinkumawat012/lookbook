from django import forms
from django.db import models
from .models import CommentModel, PostModel


class PostForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = ["image", "description"]


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentModel
        fields = ['massege', 'datetime']
