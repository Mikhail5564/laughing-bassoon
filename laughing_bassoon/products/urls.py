from django.urls import path
from .views import create_product, views_products

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('shop/', views_products, name='views_products'),
]
