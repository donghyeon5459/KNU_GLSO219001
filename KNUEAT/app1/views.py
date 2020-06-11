# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def category(request,category_name):
    shops=Shop.objects.filter(category=category_name) #category_name이 일치하는 식당만 선택
    return render(request, 'category.html',{'shops':shops,'category_name':category_name})
    
def restaurant(request, shop_id):
    shop=get_object_or_404(Shop,pk=shop_id)
    menu=Menu.objects.filter(shop=shop)
    user=request.user
    liked=Like.objects.select_related()
    if shop.likes.filter(id=user.id):
        message="즐겨찾기 취소"
    else:
        message="즐겨찾기 등록"

    return render(request, 'restaurant.html',{'shop':shop,'menu':menu, 'message':message})

def home(request):
    shop_list = Shop.objects.all().order_by('-id') #shop의 리스트를 최신 순으로 불러오기
    return render(request,'home.html', {'shops':shop_list})

def mypage_own(request):
    return render(request,'mypage_own.html')

def mypage_cus(request):
    return render(request,'mypage_cus.html')

#즐겨찾기 추가/삭제
def favorite(request, shop_id):
    user = request.user # 로그인된 유저의 객체를 가져온다.
    shop = get_object_or_404(Shop, pk=shop_id) # 좋아요 버튼을 누를 글을 가져온다.

    # 이미 좋아요를 눌렀다면 좋아요를 취소, 아직 안눌렀으면 좋아요를 누른다.
    if shop.likes.filter(id=user.id): # 로그인한 user가 현재 blog 객체에 좋아요를 눌렀다면
        shop.likes.remove(user) # 해당 좋아요를 없앤다.
    else: # 아직 좋아요를 누르지 않았다면
        shop.likes.add(user) # 좋아요를 추가한다.

    return redirect('/restaurant/' + str(market_id)) # 좋아요 처리를 하고 detail 페이지로 간다.