from django.contrib import admin
from .models import Product, Transaction, Cart


# Register your models here.
admin.site.register((Product, Transaction, Cart))
