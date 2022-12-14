from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    price = models.IntegerField()
    
    class Meta:
        db_table ="Product"
        
class Customer(models.Model):
    phone_no = models.CharField(max_length=10)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "Customer"
        
class Admin(models.Model):
    mail = models.EmailField()
    name = models.CharField(max_length=64)
    password = models.IntegerField()
    
    class Meta:
        db_table = "Admin"