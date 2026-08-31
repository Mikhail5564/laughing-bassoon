import uuid

from django.shortcuts import render, redirect
from .utils import Product, products, TOTAL_TICKETS, members, Member


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
    return render(request, 'views.html', context={'products': products})


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
        return render(request, 'tickets.html', context={"ticket_used": ticket_used,
                                                        "total_tickets": TOTAL_TICKETS})
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        if ticket_used != 0:
            members.append(Member(first_name=first_name, last_name=last_name, age=age, id=uuid.uuid4().int))
            return redirect('members')
        else:
            return render(request, 'tickets.html', context={
                "ticket_used": ticket_used,
                "total_tickets": TOTAL_TICKETS,
                "error": "ВСЕ БИЛЕТЫ ПРОДАНЫ"
            })


def members_view(request):
    return render(request, 'members_view.html', context={'members': members})


def licenses(request):
    if request.method == "GET":
        uid = None
        id = int(request.GET.get('id'))
        for item in members:
            if id == item.id:
                uid = item
                break
        return render(request, 'licenses.html', context={'member': uid})
    else:
        id = int(request.GET.get('id'))
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = int(request.POST.get('age'))
        for item in members:
            if id == item.id:
                item.first_name = first_name
                item.last_name = last_name
                item.age = age
                break
        return redirect('members')


def delete_member(request):
    id = int(request.GET.get('id'))
    for item in members:
        if id == item.id:
            members.remove(item)
    return redirect("members")
