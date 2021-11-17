from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Category


def main(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"home": "active", "posts": posts})


def about(request):
    return render(request, "about.html", {"about": "active"})


def post(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    return render(request, "post.html", {"post": post, "categories": categories})


def contact(request):
    return render(request, "contact.html", {"contact": "active"})
