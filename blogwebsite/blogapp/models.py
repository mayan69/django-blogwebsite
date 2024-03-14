from django.db import models
from django.contrib.auth.models import User

# from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Tags(models.Model):
    name= models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class BlogPost(models.Model):
    title=models.CharField(max_length= 200, verbose_name="blog title",unique=True)
    description=models.TextField()
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    thumbnail=models.ImageField(upload_to="thumbnails", default="default.jpg")
    category= models.ForeignKey(Category, on_delete=models.CASCADE ,default=1)
    tags=models.ManyToManyField(Tags, related_name="post")
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self) -> str:
        return f'{self.title}'
