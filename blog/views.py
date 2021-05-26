from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'index.html', {"posts": posts})


def post(request, slug):
    print(slug)
    return render(request, 'post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })


def about(request):
    return render(request, "about.html", {})
