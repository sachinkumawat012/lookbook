from django.contrib import admin
from .models import CommentModel, PostModel, Following

# Register your models here.

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    display_list = ['image', 'description', 'like']



@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    display_list = ['massege', 'datetime']


@admin.register(Following)
class CommentAdmin(admin.ModelAdmin):
    display_list = []
