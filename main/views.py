from django.shortcuts import redirect, render
from .models import Post

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def login(request):
    return render(request, 'main/login.html')


def signup(request):
    return render(request, 'main/signup.html')


def blog(request):
    postlist = Post.objects.all()
    # dictionary single quote 없으면 데이터 안넘어감
    return render(request, 'main/blog.html', {'postlist': postlist})


def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})


def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'post': post})
