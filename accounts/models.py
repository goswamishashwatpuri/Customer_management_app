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


# insert Class Order(): below this comment

