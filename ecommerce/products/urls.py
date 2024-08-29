# mart/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', products, name='products'),
    path('product/', product, name='product'),
    path('product/<int:product_id>/', product, name='product'), 
    
]
