from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user=User.objects.get(username=request.POST['userID'])
                return HttpResponse('이미 사용하고 있는 아이디입니다!')
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST["userID"],password=request.POST["password1"]
                )
                user.profile.name=request.POST['name']
                user.profile.phonenumber=request.POST['phone']
                user.save()
                auth.login(request,user)
                return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method =="POST":
        userID=request.POST['userID']
        password=request.POST.get('password','')
        user = auth.authenticate(request,username=userID, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return HttpResponse('userID or password is incorrect')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')