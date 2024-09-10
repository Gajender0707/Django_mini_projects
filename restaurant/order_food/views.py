from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")


def register(request):
    return render(request,"register.html")


def contact_us(request):
    return render(request,"contact_us.html")


def rough(request):
    return render(request,"rough.html")


def pizza(request):
    return render(request,"pizza.html")


def drink(request):
    return render(request,"drink.html")


def dessert(request):
    return render(request,"dessert.html")