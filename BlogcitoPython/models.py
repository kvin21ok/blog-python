from django.db import models
from django.contrib.auth.admin import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='posteos', null=True, blank=True)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    send_date = models.DateField(auto_now_add=True)