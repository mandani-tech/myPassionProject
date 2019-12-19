from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    itemName = models.CharField(max_length=100)
    itemNumber = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    inStock = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    dept = models.CharField(max_length=500)
    subDept= models.CharField(max_length=500)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank = True)
    products = models.ManyToManyField(Product, blank = True)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    updated = models.DateTimeField(auto_now= True)
    timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.id)
