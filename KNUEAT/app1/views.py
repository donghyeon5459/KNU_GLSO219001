# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone
import collections
import random
# Create your views here.
def category(request,category_name):
    shops=Shop.objects.filter(category=category_name) #category_name이 일치하는 식당만 선택
    return render(request, 'category.html',{'shops':shops,'category_name':category_name})
    
def restaurant(request, shop_id):
    shop=get_object_or_404(Shop,pk=shop_id)
    menu=Menu.objects.filter(shop=shop)
    user=request.user
    liked=Like.objects.select_related()
    reviews=Review.objects.filter(shop=shop)
    reservations = Reservation.objects.filter(customer=user)
    if shop.likes.filter(id=user.id):
        message="즐겨찾기 취소"
    else:
        message="즐겨찾기 등록"

    return render(request, 'restaurant.html',{'shop':shop,'menu':menu, 'message':message, 'reviews':reviews, 'reservations': reservations})

def home(request):
    
    if request.method == 'POST':
        shop_name=request.POST['shop_name']
        shop=Shop.objects.filter(name__contains=shop_name)
        return render(request,'search.html',{'shop':shop,'shop_name':shop_name})

    user=request.user

    if user.is_active:
        likes=Like.objects.select_related()
        if(Reservation.objects.filter(customer=user)):
            recommend_shop=recommendation(Reservation.objects.filter(customer=user))
        else:
            recommend_shop=random_rec()
        if user.profile.shop_id == -1:
            return render(request, 'home.html', {'user':user, 'likes':likes, 'recommends':recommend_shop})
        else:
            shop=get_object_or_404(Shop, pk=user.profile.shop_id)
            return render(request, 'home.html', {'user':user, 'shop': shop, 'likes':likes,'recommends':recommend_shop})
    else:
        recommend_shop=random_rec()
        return render(request, 'home.html', {'user':user, 'recommends': recommend_shop})


def mypage_own(request):
    user = request.user
    my_shop=Shop.objects.filter(owner = user)
    #number = temp[:3]+'-'+temp[3:7]+"-"+temp[7:]
    return render(request,'mypage_own.html', {'my_shop': my_shop})


def mypage_cus(request):
    user=request.user
    likes=Like.objects.select_related()
    return render(request,'mypage_cus.html', {'likes': likes})

def register_store_page(request):
    return render(request,'register_store_page.html')

def register_store(request):
    user = request.user
    shop=Shop()
    shop.name=request.POST['가게명']
    shop.address=request.POST['가게주소']
    shop.phone_number=request.POST['가게연락처']
    shop.open_time = request.POST['오픈시간']
    shop.close_time = request.POST['닫는시간']
    shop.category = request.POST['카테고리']
    shop.photo = request.FILES['photo']
    if( not shop.photo ):
        print()#수정할것
        #shop.photo = 
    shop.description = request.POST['가게설명']
    shop.owner = user
    shop.save()

    user.profile.shop_id = shop.id
    return redirect('/')

def register_menu(request):
    if request.method == 'POST':
        menu=Menu(name=request.POST['name'],price=request.POST['price'],photo=request.FILES['photo'])
        user=request.user
        #print(user)
        shop=get_object_or_404(Shop,owner=user.id)
        menu.shop=shop
        menu.save()
        return redirect('/')
    return render(request,'register_menu.html')


#즐겨찾기 추가/삭제
def favorite(request, shop_id):
    user = request.user # 로그인된 유저의 객체를 가져온다.
    shop = get_object_or_404(Shop, pk=shop_id) # 좋아요 버튼을 누를 글을 가져온다.

    # 이미 좋아요를 눌렀다면 좋아요를 취소, 아직 안눌렀으면 좋아요를 누른다.
    if shop.likes.filter(id=user.id): # 로그인한 user가 현재 blog 객체에 좋아요를 눌렀다면
        shop.likes.remove(user) # 해당 좋아요를 없앤다.
    else: # 아직 좋아요를 누르지 않았다면
        shop.likes.add(user) # 좋아요를 추가한다.

    return redirect('/restaurant/' + str(shop_id)) # 좋아요 처리를 하고 detail 페이지로 간다.

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
    #print (current_user.id)
    reservation=Reservation.objects.filter(customer_id=current_user.id)
    return render(request,'reservation_done.html',{'reservation':reservation})


def register_review(request, shop_id):
    if request.method == 'POST':
        user = request.user
        shop = get_object_or_404(Shop, pk=shop_id)
        time=timezone.now().strftime("%H:%M:%S")
        review = Review(time=time,rating=request.POST['score'],comment = request.POST['review_text'])
        #review.time = timezone.now()
        #review.rating = request.POST['displayStarRating']
        #review.comment = request.POST['review_text']
        review.shop = shop
        review.user = user
        review.save()
        return redirect('/restaurant/'+str(shop_id))

    return render(request, 'restaurant.html')

def like(request):
    likes=Like.objects.select_related()
    user=request.user
    #print(likes)
    return render(request,'like.html', {'likes':likes})

def recommendation(reservation):
    reserv_list=list(reservation)
    cate_list=[]
    #print("*********************************************")
    for el in reserv_list:
        cate_list.append(el.shop.category)
    cnt_dict=collections.Counter(cate_list)
    for el in cnt_dict.most_common(1):
        most=el[0]
    #print(Shop.objects.filter(category=most))
    shop_lst=Shop.objects.filter(category=most)

    shop_dict=dict()
    for el in shop_lst:
        shop_dict[el]=el.like_count()
    #print(shop_dict)
    Max=max(shop_dict.values())
    for key,val in shop_dict.items():
        if (val==Max):
            return key

def random_rec():
    shop_list=list(Shop.objects.all())
    random.shuffle(shop_list)
    #print(shop_list[0])
    return shop_list[0]
