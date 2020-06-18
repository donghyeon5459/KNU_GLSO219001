from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    name=models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    phone_number=models.CharField(max_length=225)
    open_time=models.TimeField()
    close_time=models.TimeField()
    category=models.CharField(max_length=225)
    description=models.TextField()
    photo=models.ImageField(upload_to='images/')
    owner=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    likes =models.ManyToManyField(
        User, # User 모델과 Shop 모델을 M : N 관계로 두겠다.
        through='Like', # Like라는 중개 모델을 통해 M : N 관계를 맺는다.
        through_fields=('shop', 'user'), # Like에 shop 속성, user 속성을 추가하겠다.
        related_name='likes' # 1 : N  관계에서 market과 연결된 comment를 가져올 때 comment_set으로 가져왔는데, 
                            # related_name을 설정하면 shop.like_set이 아니라 shop.likes로 shop과 연결된 like를 가져올 수 있다.
        )

    def __str__(self):
        return self.name

    # 몇 개의 like와 연결되어 있는가를 보여준다.
    def like_count(self):
        return self.likes.count()

class Like(models.Model):
    # Shop의 through_fields와 순서가 같아야 한다.
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True) # 특정 market이 삭제되면, 그 market의 즐겨찾기 정보 제거
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Reservation(models.Model):
    group_name=models.CharField(max_length=225)
    time=models.CharField(max_length=225) #models.DateTimeField(auto_now_add=True)
    requirements=models.CharField(max_length=225)
    confirmed=models.IntegerField(default=0)
    customer=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    num=models.IntegerField(default=0)
    def __str__(self):
        return self.group_name
        
class Menu(models.Model):
    name=models.CharField(max_length=225)
    price=models.IntegerField()
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    photo=models.ImageField(upload_to='images/menu', default="")
    def __str__(self):
        return self.name
    
class Review(models.Model):
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
    

