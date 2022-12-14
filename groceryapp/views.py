from django.http import JsonResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from groceryapp.serializers import AdminSerializers, CustomerSerializers, ProductSerializers
from groceryapp.models import Admin, Customer, Product

# Create your views here.

@api_view(['GET', 'POST'])
def get_Product(request):
    if request.method == "GET":
        data=request.data
        query= Product.objects.all()
        serializers = ProductSerializers(query, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif request.method == "POST":
        prod_query = ProductSerializers(data=request.data)
        if prod_query.is_valid():
            prod_query.save()
        return JsonResponse(prod_query.data)

       
@api_view(['GET', 'POST'])
def set_Customer(request):
    if request.method == "GET":
        data=request.data
        query= Customer.objects.all()
        serializers = CustomerSerializers(query, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif request.method == "POST":
        cust_query = CustomerSerializers(data=request.data)
        if cust_query.is_valid():
            cust_query.save()
        return JsonResponse(cust_query.data)

@api_view(['GET', 'POST', 'DELETE'])
def gett_Admin(request):
    if request.method == "GET":
        data=request.data
        query= Admin.objects.all()
        serializers = AdminSerializers(query, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif request.method == "POST":
        ad_query = AdminSerializers(data=request.data)
        if not ad_query.is_valid():
            return JsonResponse(ad_query.errors)
            
        ad_query.save()
        
    return JsonResponse(ad_query.data)
