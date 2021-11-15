from django.urls import path
from django.urls import path
from .views import about, contact, main, post

app_name='blog'

urlpatterns =[
    path("", main, name='main'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("post/", post, name='post')
]
