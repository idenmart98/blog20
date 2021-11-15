from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=150)
    creat_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
