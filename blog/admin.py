from django.contrib import admin
from .models import Post, Category, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'creat_at']
    list_filter = [
        "category"
    ]
    search_fields = [
        "title",
        "description"
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)