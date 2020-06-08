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

'''
데이터 베이스 관련 view.py 참조 코드

def home(request):
    blogs = Blog.objects.all().order_by('-id') #쿼리셋을 들고옴.

    #Blog의 모든 객체들이 쿼리셋 형식으로 templates에 보내짐.
    return render(request, 'blog/home.html',{'blogs':blogs})

def detail(request, blog_id):
    detail = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/detail.html',{'detail':detail})

def new(request):
    return render(request,'blog/new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date =timezone.datetime.now()
    blog.save()

    return redirect('/blog/'+str(blog.id))

def edit(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)#특정 객체 가져오기
    return render(request,'blog/edit.html',{'blog':blog})

def update(request,blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)#특정 객체 가져오기
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date =timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request,blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)#특정 객체 가져오기
    blog.delete()
    return redirect('home')
'''
    

