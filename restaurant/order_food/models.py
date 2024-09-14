from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class order_details(models.Model):

    #creating the user detaisl for the login and resgitering the details...
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    #creating the feilds for the adding the details of the Order....
    order_id=models.IntegerField(null=False)
    item_name=models.CharField(max_length=100,null=True)
    item_quantity=models.IntegerField(null=True)
    item_price=models.IntegerField(null=True)
    date=models.DateField()
    time=models.TimeField()
