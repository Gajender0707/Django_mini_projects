pizza_price_details={
            "cheez_pizza":100,
            "veggie_pizza":89,
            "pepperoni_pizza":120,
            "meat_pizza":160,
            "margherita_pizza":129,
            "bbq_chicken_pizza":189
        }

pizza_name="pepperoni_pizza"

for name,price in pizza_price_details.items():
    if name==pizza_name:
        print(name,price)