from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    publish_date = models.DateField()