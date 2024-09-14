from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from random import randint

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
        # print(data)
        pizza_price_details={
            "none":0,
            "cheez_pizza":99,
            "veggie_pizza":89,
            "pepperoni_pizza":120,
            "meat_pizza":160,
            "margherita_pizza":129,
            "bbq_chicken_pizza":189
        }

        drink_price_details={
            "none":0,
            "cold_coffee":120,
            "iced_tea":99,
            "coke":75,
            "beer":140,
            "lemonade":119,
            "sparkling_water":79
        }


        dessert_price_details={
            "none":0,
            "gulab_jamun":30,
            "kulfi":49,
            "brownie":89,
            "rasmalai":99,
            "tiramisu":110,
            "phirni":79
        }


        pizza_price=0
        drink_price=0
        dessert_price=0

        ## validating the price...

        for name,price in pizza_price_details.items():
            if name==pizza_name:
                pizza_price=price

        for name,price in drink_price_details.items():
            if name==drink_name:
                drink_price=price


        for name,price in dessert_price_details.items():
            if name==dessert_name:
                dessert_price=price



       ## Creating the data dict....
        my_data={
            "Items_name":[pizza_name,drink_name,dessert_name],
            "Items_quantity":[pizza_quantity,drink_quantity,dessert_quantity],
            "Items_price":[pizza_price,drink_price,dessert_price],
        }
        
        order_id=randint(1,10000)
        ##zipping the file for the uploading to the order-detail file and load there multiple data...
        combined_order_data = zip(my_data['Items_name'], my_data['Items_quantity'], my_data['Items_price'])
        #creting the total file...
        total=[ int(i)*int(j) for i,j in zip(my_data["Items_price"],my_data["Items_quantity"])]
        my_data["total"]=total
        combined_order_data = zip(my_data['Items_name'], my_data['Items_quantity'], my_data['Items_price'],my_data["total"])
        overall_total=sum(my_data["total"])

        context={"data":combined_order_data,"overall_total":overall_total,"order_id":order_id,"order_date":datetime.now()}


        ##Creating the objects and uploading the dataset to the db....
        
        for i in range(len(my_data['Items_name'])):
            if my_data['Items_name'][i]=='none' or my_data['Items_name'][i]==None:
                continue
            else:

                print(my_data['Items_name'][i])
                print(my_data['Items_quantity'][i])
                print(my_data['Items_price'][i])

                order_details.objects.create(
                    order_id=order_id,
                    item_name=my_data["Items_name"][i],
                    item_quantity=int(my_data["Items_quantity"][i]),
                    item_price=int(my_data["Items_price"][i]),
                    date=datetime.now(),
                    time=datetime.now()
                )


        return render(request,"order_detail.html",context)
    return render(request,"order_food.html")


def order_detail(request):
    return render(request,"order_detail.html")

