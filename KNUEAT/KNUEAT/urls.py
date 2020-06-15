# -*- coding: utf-8 -*-
"""KNUEAT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import app1.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),
    path('',app1.views.home, name="home"),
    path('category/<str:category_name>/',app1.views.category, name="category"),
    path('restaurant/<int:shop_id>',app1.views.restaurant, name="restaurant"),
    path('mypage_own/', app1.views.mypage_own, name='mypage_own'),
    path('mypage_cus/', app1.views.mypage_cus, name='mypage_cus'),
    path('register_store_page/', app1.views.register_store_page, name='register_store_page'),
    path('register_store/', app1.views.register_store, name='register_store'),
    path('reservation/<int:id>/',app1.views.reservation,name='reservation'),
    path('reservation_manage/',app1.views.reservation_manage,name='reservation_manage'),
    path('reservation_done/',app1.views.reservation_done,name='reservation_done'),
    path('favorite/<int:id>',app1.views.favorite,name='favorite'),
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
