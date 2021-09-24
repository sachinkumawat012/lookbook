from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.db.models.fields.related import ManyToManyField
# Create your models here.


class PostModel(models.Model):
    user = models.ManyToManyField(User)
    image = models.ImageField(upload_to="profilepic", null=True, blank=True)
    description = models.CharField(max_length=500)
    like = ManyToManyField(User, related_name='likes')

    def total_likes(self):
        return self.like.count()
    

class CommentModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    massege = models.TextField('massege', null=True, blank=True)
    datetime = models.DateTimeField(default=date.today)


class Following(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, related_name="followed")

    @classmethod
    def follow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user=user)
        obj.followed.add(another_account)
        print("followed")

    @classmethod
    def unfollow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user=user)
        obj.followed.remove(another_account)
        print("unfollowed")

    def __str__(self):
        return str(self.user)