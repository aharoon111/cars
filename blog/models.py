from django.db import models
from datetime import datetime    
from django.utils.timezone import now



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=now, editable=True)
    

def __str__(self):
    return self.description

