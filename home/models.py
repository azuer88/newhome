from django.db import models

class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField()
