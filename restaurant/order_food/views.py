from django.shortcuts import render,redirect

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
    button_text="Add to Bucket"
    if request.method=="POST":
        button_text="Added"
        return render(request,"rough.html",context={"button_text":button_text})
    return render(request,"rough.html")


def pizza(request):
    return render(request,"pizza.html")


def drink(request):
    return render(request,"drink.html")


def dessert(request):
    return render(request,"dessert.html")


def privacy(request):
    return render(request,"privacy.html")

def terms(request):
    return render(request,"terms.html")

def order_food(request):
    if request.method=="POST":
        data=request.POST
        pizza_name=data.get("pizza")
        pizza_quantity=data.get("pizza_quantity")
        drink_name=data.get("drink")
        drink_quantity=data.get("drink_quantity")
        dessert_name=data.get("dessert")
        dessert_quantity=data.get("dessert_quantity")
        # print(pizza_name,pizza_quantity,drink_name,drink_quantity,dessert_name,dessert_quantity)
        context={"data":data}
        return render(request,"order_detail.html",context)
    return render(request,"order_food.html")


def order_detail(request):
    return render(request,"order_detail.html")

