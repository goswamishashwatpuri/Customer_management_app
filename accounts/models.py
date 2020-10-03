from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(blank=True, default= " ", upload_to='images/' )

    # For showing the name of Customer in admin panel rathe than { Customer_object(1) }
    def __str__(self):
        return self.name


class Product(models.Model):

    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Out door'),
    )

    name = models.CharField(max_length=100, null =True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null =True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    description =  models.CharField(max_length=100, null =True)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=100, null=True)

    # For showing the name of Tag in admin panel rathe than { Customer_object(1) }
    def __str__(self):
        return self.name

class Order(models.Model):

    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered'),
    )

    Customer = models.ForeignKey(Customer, null=True, blank=True, on_delete= models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)

    status = models.CharField(max_length=100, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.Product.name + ' : ' + self.Customer.name
