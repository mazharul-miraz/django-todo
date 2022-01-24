from unicodedata import name
from django.db import models

# Create your models here.

class TodoModel(models.Model):
    name = models.TextField(max_length=100)
    email =models.EmailField(max_length=100)
    
    ACTIVITY_CHOICES = (
    ('active','ACTIVE'),
    ('inactive', 'INACTIVE'),
    )
    
    activity = models.CharField(max_length=10,choices=ACTIVITY_CHOICES,default='inactive')
  
    