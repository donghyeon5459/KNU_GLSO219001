# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def category(request,category_name):
    shops=Shop.objects.filter(category=category_name) #category_name이 일치하는 식당만 선택
    return render(request, 'category.html',{'shops':shops,'category_name':category_name})
    
def restaurant(request,id):
    shop=get_object_or_404(Shop,pk=id)
    menu=Menu.objects.filter(shop=shop)
    return render(request, 'restaurant.html',{'shop':shop,'menu':menu})

def home(request):
    shop_list = Shop.objects.all().order_by('-id') #shop의 리스트를 최신 순으로 불러오기
    return render(request,'home.html', {'shops':shop_list})