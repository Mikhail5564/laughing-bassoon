from django.urls import path
from .views import create_product, views_products, views_product, tickets

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('shop/', views_products, name='views_products'),
    path('product/', views_product, name='views_product'),
    path('tickets/', tickets, name='tickets'),
]
