import imp
from django.contrib import admin

# Register your models here.
from .models import TododataModel

admin.site.register(TododataModel)