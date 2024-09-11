order_data = {
        'Items_name': ['meat_pizza', 'coke', 'rasmalai'],
        'Items_quantity': [2,1,3],
        'Items_price': [160, 75, 99],
    }


total=[ i*j for i,j in zip(order_data["Items_price"],order_data["Items_quantity"])]

print(total)
order_data["total"]=total

print(order_data)


    