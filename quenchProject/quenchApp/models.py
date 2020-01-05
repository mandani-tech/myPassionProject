from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
# Create your models here.



class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs=self.objects.id
        print(qs)
        if qs.count()==1:
            return qs.first()
        return None #Todo fix this to show all the products objects


class Product(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    itemName = models.CharField(max_length=100)
    itemNumber = models.CharField(max_length=100)
    description = models.TextField(default="Description")
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    inStock = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2, default=00.00)
    dept = models.CharField(max_length=500)
    subDept= models.CharField(max_length=500)
#
#     objects = ProductManager()
    def __str__(self):
            return str(self.itemName)




class CartManager(models.Manager):
    def get_user_obj():
        return user_obj

    def new(self,request,user=None,):
        print(user)
        user_obj = None
        if user is not None:
            if request.user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank = True)
    products = models.ManyToManyField(Product, blank = True , null =True)
    subtotal = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=0)
    tax = models.DecimalField(default=0.00,max_digits=100,decimal_places=0)
    updated = models.DateTimeField(auto_now= True)
    timestamp = models.DateTimeField(auto_now_add= True)

    objects= CartManager()

    def __str__(self):
        return str(self.id)
