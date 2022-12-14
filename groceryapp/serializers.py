from rest_framework import serializers
from groceryapp.models import Admin, Customer, Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code', 'name', 'category', 'price')

    def create(self,data):
        instance = Product.objects.create(**data)
        return instance 

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = ('phone_no', 'name')

    def create(self,data):
        instance = Customer.objects.create(**data)
        return instance        

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin 
        fields = ('mail', 'name', 'password')

    def create(self,data):
        instance = Admin.objects.create(**data)
        return instance                