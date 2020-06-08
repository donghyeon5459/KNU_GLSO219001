from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    name=models.CharField(max_length=225)
    adress=models.CharField(max_length=225)
    phone_number=models.CharField(max_length=225)
    open_time=models.CharField(max_length=225)
    close_time=models.CharField(max_length=225)
    category=models.CharField(max_length=225)
    description=models.TextField()
    photo=models.ImageField(upload_to='images/')
    owner=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Reservation(models.Model):
    group_name=models.CharField(max_length=225)
    time=models.CharField(max_length=225) #models.DateTimeField(auto_now_add=True)
    requirements=models.CharField(max_length=225)
    confirmed=models.IntegerField(default=0)
    customer=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

class Menu(models.Model):
    name=models.CharField(max_length=225)
    price=models.IntegerField()
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    
class Review():
    time=models.CharField(max_length=225)
    rating=models.IntegerField()
    comment=models.TextField()
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

