# Generated by Django 3.2.7 on 2021-09-27 10:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0010_auto_20210924_1603'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostModel',
            new_name='Post',
        ),
    ]
