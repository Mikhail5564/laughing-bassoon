from django.shortcuts import render, redirect
from .utils import Product, products, TOTAL_TICKETS, members

def create_product(request):
    if request.method == "GET":
        return render(request, 'create.html')
    else:
        name = request.POST.get('name')
        description = request.POST.get('description')
        count = request.POST.get('count')
        price = request.POST.get('price')
        products.append(Product(name=name, description=description, count=count, price=price))
        return redirect("views_products")


def views_products(request):
    return render(request, 'views.html' , context={'products': products})


def views_product(request):
    name = request.GET.get('name')
    for item in products:
        if name == item.name:
            res = item
            break
    return render(request, 'view_product.html', context={'product': res})




def tickets(request):
    ticket_used = TOTAL_TICKETS - len(members)
    if request.method == "GET":
        return render(request, 'tickets.html', context={"ticket_used": ticket_used,"total_tickets": TOTAL_TICKETS})