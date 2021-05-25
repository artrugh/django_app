from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'index.html', {"posts": posts})


def post(request):
    return HttpResponse("I am a single post page.")
