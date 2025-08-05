from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES =[('pending','pending'),('confirmed' ,'confirmed '),('delivered','delivered'),('cancelled','cancelled'),]
    customer =models.ForeignKey(User,on_delete =models.CASCADE,related_name ='orders')
    order_items =models.ManyToManyField(Menu,related_name='orders')
    total_amount= models.DecimalField(max_digits=10,decimal_places=2)
    status =models.CharField(max_length=20,choices =STATUS_CHOICES,default='pending')
    ordered_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)