from unicodedata import name
from django.db import models

# Create your models here.

class TododataModel(models.Model):
    name = models.TextField(max_length=500)
    email =models.EmailField(max_length=100)