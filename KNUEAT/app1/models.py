from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    name=models.CharField(max_length=225)
    adress=models.CharField(max_length=225)
    phone_number=models.CharField(max_length=225)
    open_time=models.CharField(max_length=225)
    close_time=models.CharField(max_length=225)
    description=models.TextField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo=models.ImageField(upload_to='images/')

class Menu(models.Model):
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    
class Review():
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

