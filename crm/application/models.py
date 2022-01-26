from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length= 45, null = True)
    last_name = models.CharField(max_length= 45, null = True)
    email = models.CharField(max_length= 45, null = True)
    phone = models.CharField(max_length= 45, null = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length= 200, null = True)
    description = models.CharField(max_length= 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product,null = True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    status = models.CharField(max_length=200,null = True, choices = STATUS)