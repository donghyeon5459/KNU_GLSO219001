# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
#from .models import

# Create your views here.
def category(request):
    return render(request, 'category.html')
    
def restaurant(request):
    return render(request, 'restaurant.html')

def home(request):
    return render(request,'home.html')