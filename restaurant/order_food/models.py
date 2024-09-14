from django.db import models

# Create your models here.

class customer_details(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)


class order_details(models.Model):
    order_id=models.IntegerField(null=False)
    item_name=models.CharField(max_length=100,null=True)
    item_quantity=models.IntegerField(null=True)
    item_price=models.IntegerField(null=True)
    date=models.DateField()
    time=models.TimeField()
