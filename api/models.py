
from django.db import models

# Create your models here.

class Task(models.Model):
  user_name = models.CharField(max_length=200)
  caption = models.CharField(max_length=200)
  image_url = models.URLField(max_length=500)
      
  def __str__(self):
    return self.user_name