from django.shortcuts import render
from .models import Post


def base(request):
    return render(request,'base.html')

def home(request):
    posts=Post.objects.all()
    context={
        'posts': posts
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')
