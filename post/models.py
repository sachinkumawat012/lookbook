from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserPostModel(models.Model):
    post_of_user = models.ManyToManyField(User)
    image = models.ImageField(upload_to="profilepic", null=True, blank=True)
    description = models.CharField(max_length=500)
