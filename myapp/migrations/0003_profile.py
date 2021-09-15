# Generated by Django 3.2.4 on 2021-09-14 14:21

import builtins
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profilepic')),
                ('caption', models.CharField(max_length=500)),
                ('profile_of_user', models.OneToOneField(on_delete=builtins.callable, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]