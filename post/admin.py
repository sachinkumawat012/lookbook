from django.contrib import admin
from .models import Comment, Follower, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    display_list = ['image', 'description', 'likes', 'username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    display_list = ['massege', 'datetime']


@admin.register(Follower)
class FollowAdmin(admin.ModelAdmin):
    display_list = ['']

