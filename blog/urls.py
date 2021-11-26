from django.urls import path
from django.urls import path
from .views import about, contact, main, post, comment_create, red

app_name = 'blog'

urlpatterns =[
    path("", main, name='main'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("post/<int:pk>/", post, name='post'),
    path("comment/create/", comment_create, name="comment_create"),
    path("red/", red, name="red")
]
