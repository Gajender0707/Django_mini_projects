from django.urls import path,include
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("contact_us/",views.contact_us,name="contact_us"),
    path("rough/",views.rough,name="rough"),
    path("pizza/",views.pizza,name="pizza"),
    path("drink/",views.drink,name="drink"),
    path("dessert/",views.dessert,name="dessert"),
    path("privacy/",views.privacy,name="privacy"),
    path("terms/",views.terms,name="terms"),
    path("order_food/",views.order_food,name="order_food")
]
