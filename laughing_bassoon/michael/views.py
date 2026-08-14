from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_currency


def my_view(request):
    return render(request, 'hello.html')


def my_view1(request):
    return HttpResponse("<h1>Hello</h1>")

def my_view2(request):
    return HttpResponse("<h1>World</h1>")

def operation(request):
    arg = int(request.GET.get('number1',50))
    arg2 = int(request.GET.get('number2',10))
    arg3 = request.GET.get('operate',"-")
    print(arg3)
    return HttpResponse(f"<h1>{arg - arg2 if arg3 == "-" else arg + arg2}</h1>")

def sos_help(request):
    number = int(request.GET.get('number', 4))
    context = {"name": "Экстренные службы"}
    if number == 1:
        context["message"] = "пожарную часть"
    elif number == 2:
        context["message"] = "полицию"
    elif number == 3:
        context["message"] = "скорую помощь"
    else:
        context["message"] = ("экстренную службу (нажмите 1 если хотите позвонить в пожарную часть,нажмите 2 если хотите"
                              "позвонить в полицию,нажмите 3 если хотите позвонить в скорую помощь)")
    return render(request, "numbers.html", context)


def square(request):
    number = int(request.GET.get('number', 4))
    context = {"name": [item ** 2 for item in range(1, number + 1)]}
    return render(request, "test.html", context)


def shop(request):
    id = int(request.GET.get('number', 0))
    context = {}
    if id == 1:
        context["name"] = "Нож Классический"
        context["price"] = 1200
        context["count"] = 20
    elif id == 2:
        context["name"] = "Револьвер ACR"
        context["price"] = 2321
        context["count"] = 10
    elif id == 3:
        context["name"] = "Винтовка AWP"
        context["price"] = 4500
        context["count"] = 5
    else:
        context["name"] = "Такой страницы не существует"

    return render(request, "shop.html", context)


def calculate(request):
    if request.method == "GET":
        return render(request, "calculation.html")
    else:
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        action = request.POST.get("action")
        if action == "+":
            result = num1 + num2
        elif action == "-":
            result = num1 - num2
        elif action == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        return render(request, "calculation.html", context={"result": result})


def converter(request):
    dollar = get_currency("USD")
    euro = get_currency("EURO")
    cny = get_currency("CNY")
    context = {"usd": dollar, "eur": euro, "cny": cny}
    if request.method == "GET":
        return render(request, "converter.html",context)
    else:
        rub_amount = float(request.POST.get("rub_amount"))
        checkbox_amount = request.POST.get("currency")
        values = {"USD": dollar, "EUR": euro, "CNY": cny}
        if checkbox_amount:
            result = rub_amount / values[checkbox_amount]
            context["res"] = round(result, 2)
        else:
            context["error"] = 'Ошибка выбора валюты!'
        context["currency"] = checkbox_amount
        return render(request, "converter.html", context)

def event(request):
    if request.method == "GET":
        return render(request, "event.html")
    else:
        name = request.POST.get("first_name")
        surname = request.POST.get("last_name")
        return render(request, "ticket.html", context={"name": name, "surname": surname})
