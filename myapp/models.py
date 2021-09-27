from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'profilepic', null=True, blank=True)
    caption = models.CharField(max_length=500)


# class Post(models.Model):

#     by_user = models.ManyToManyField(User)


# class Like(models.Model):

#     from_user = models.ManyToManyField(User)


# class Comment(models.Model):

#     from_user = models.ManyToManyField(User)
    

# class Follow(models.Model):

#     to_user_from_user =  models.ManyToManyField(User)