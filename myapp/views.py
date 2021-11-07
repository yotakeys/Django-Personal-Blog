from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render (request, 'index.html', {'posts': posts})

def post(request,title):
    posts=Post.objects.get(title=title)
    return render (request, 'post.html', {'posts':posts})