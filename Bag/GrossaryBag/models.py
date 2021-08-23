from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GroceryList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=256)
    item_quantity = models.CharField(max_length=50)
    item_status = models.CharField(max_length=100)
    date = models.DateField()
