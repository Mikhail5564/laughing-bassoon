from django.shortcuts import render, redirect
from .utils import Product, products

def create_product(request):
    if request.method == "GET":
        return render(request, 'create.html')
    else:
        name = request.POST.get('name')
        description = request.POST.get('description')
        count = request.POST.get('count')
        price = request.POST.get('price')
        products.append(Product(name=name, description=description, count=count, price=price))
        print(products)
        return redirect("views_products")


def views_products(request):
    return render(request, 'views_products.html' , context={'products': products})