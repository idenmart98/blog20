from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def main(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"home": "active", "posts": posts})


def about(request):
    return render(request, "about.html", {"about": "active"})


def post(request):
    return render(request, "post.html", {"post": "active"})


def contact(request):
    return render(request, "contact.html", {"contact": "active"})
