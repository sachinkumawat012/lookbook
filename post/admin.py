from django.contrib import admin
from .models import CommentModel, Followers, PostModel

# Register your models here.

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    display_list = ['image', 'description', 'like', 'username']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    display_list = ['massege', 'datetime']


@admin.register(Followers)
class FollowAdmin(admin.ModelAdmin):
    display_list = ['']

