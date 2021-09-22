from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class PostModel(models.Model):
    user = models.ManyToManyField(User)
    image = models.ImageField(upload_to="profilepic", null=True, blank=True)
    description = models.CharField(max_length=500)


class CommentModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    massege = models.TextField('massege', null=True, blank=True)
    datetime = models.DateTimeField(default=date.today)
