from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ERBOL" 

class Post(models.Model):
    title = models.CharField(max_length=150)
    creat_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    short_description = models.TextField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=15, verbose_name="Автор")
    description = models.TextField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.author} -> {self.post}'
