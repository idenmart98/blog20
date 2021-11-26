from django import forms
from django.shortcuts import redirect, render

from .forms import CommentCreateForm
from .models import Post, Category


def main(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"home": "active", "posts": posts})


def about(request):
    return render(request, "about.html", {"about": "active"})


def post(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentCreateForm()
    categories = Category.objects.all()
    return render(request, "post.html", {
        "post": post,
        "categories": categories,
        "comment_form": comment_form})


def contact(request):
    return render(request, "contact.html", {"contact": "active"})

def comment_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = CommentCreateForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            print(1)
            instance = form.save()
            return redirect("blog:post", pk=instance.post.id)
    return redirect("blog:main")


def red(request):
    print(request.GET['red'])
    print(request.GET['green'])