from django.db import models
from django.db.models.base import Model
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    context= models.CharField(max_length=1000000000000)
    date= models.DateTimeField(default=datetime.now, blank=True)