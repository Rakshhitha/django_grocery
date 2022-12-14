from django.urls import path, include
from  . import views

urlpatterns=[
    path('get',views.get_Product, name='product'),
    path('set',views.set_Customer, name='customer'),
    path('gett',views.gett_Admin, name='admin'),
]