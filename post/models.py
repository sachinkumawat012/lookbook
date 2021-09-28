from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.db.models.fields.related import ManyToManyField
# Create your models here.


class Post(models.Model):
    user = models.ManyToManyField(User)
    image = models.ImageField(upload_to="profilepic", null=True, blank=True)
    description = models.CharField(max_length=500)
    likes = ManyToManyField(User, related_name='likes')
  

    def total_likes(self):
        return self.likes.count()
    

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    massege = models.TextField('massege', null=True, blank=True)
    datetime = models.DateTimeField(default=date.today)



class Follower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #current user
    another_user = models.ManyToManyField(User, related_name='another_user') # to be followed

    def __str__(self):
        return self.user.name


