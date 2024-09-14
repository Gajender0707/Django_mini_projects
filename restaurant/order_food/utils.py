from random import randint
# import uuid
# order_id="abc123"
# order_data = {
#         'Items_name': ['meat_pizza', 'coke', 'none'],
#         'Items_quantity': [2,1,3],
#         'Items_price': [160, 75, 99],
#     }
# total=[ i*j for i,j in zip(order_data["Items_price"],order_data["Items_quantity"])]
# order_data["total"]=total
# print(order_data)

# f_data={}

# for i in range(len(order_data['Items_name'])):
#     if order_data['Items_name'][i]=='none' or order_data['Items_name'][i]==None:
#         continue
#     else:
#         print(order_data['Items_name'][i])
#         print(order_data['Items_quantity'][i])
#         print(order_data['Items_price'][i])


# for i in range(len(order_data['Items_name'])):
#             if order_data['Items_name'][i]=="none":
#                     continue
#                     print("yes")
#             else:
#                 print(order_data['Items_name'][i])
    


weather=["sunny","fog","rainy"]
print(weather[randint(0,2)])