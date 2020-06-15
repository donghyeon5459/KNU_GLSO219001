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
    user = request.user
    temp = user.profile.phonenumber
    number = temp[:3]+'-'+temp[3:7]+"-"+temp[7:]
    return render(request,'mypage_own.html' ,{'num':number})


def mypage_cus(request):
    user=request.user
    return render(request,'mypage_cus.html')

def register_store_page(request):
    return render(request,'register_store_page.html')

def register_store(request):
    user = request.user
    
    shop=Shop()
    shop.name=request.GET['가계명']

    shop.address=request.GET['가게주소']
    shop.phone_number=request.GET['가게연락처']
    shop.open_time = request.GET['오픈시간']
    shop.close_time = request.GET['닫는시간']
    shop.category = request.GET['카테고리']
    shop.photo = request.GET['photo']
    shop.description = request.GET['가게설명']
    shop.owner = user
    shop.save()

    user.profile.shop_id = shop.id
    return redirect('/')


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

def reservation(request,id):
    if request.method == 'POST':
        reservation=Reservation(group_name=request.POST['name'],time=request.POST['time'],num=request.POST['num'],
        requirements=request.POST['requirement'])
        user=request.user
        shop=get_object_or_404(Shop,pk=id)
        reservation.customer=user
        reservation.shop=shop
        reservation.save()
        return redirect('/')
    shop=get_object_or_404(Shop,pk=id)
    return render(request,'reservation.html',{'shop':shop})

def reservation_manage(request):
    user=request.user
    #shop_id=user.id
    shop=get_object_or_404(Shop,owner=user.id)
    reservation=shop.reservation_set.all()
    if request.method=='POST':
        data=request.POST.get('승인','취소')
        if data=='승인':
            num=request.POST['hidden']
            reserv=Reservation.objects.filter(id=num)[0]
            reserv.confirmed=1
            reserv.save()
        else:
            num=request.POST['hidden']
            reserv=Reservation.objects.filter(id=num)
            reserv.delete()

    return render(request,'reservation_manage.html',{'reservation':reservation,'id':id})

def reservation_done(request):
    current_user=request.user
    print (current_user.id)
    reservation=get_object_or_404(Reservation,customer_id=current_user.id)
    return render(request,'reservation_done.html',{'reservation':reservation})