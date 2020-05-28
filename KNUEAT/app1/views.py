# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,"signup.html")

def category(request):
    return render(request, 'category.html')
    
def restaurant(request):
    return render(request, 'restaurant.html')