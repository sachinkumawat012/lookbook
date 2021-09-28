from django import forms
from django.db import models
from .models import Comment, Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["image", "description"]


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['massege', 'datetime']
