from django.db import models
from django.contrib.auth.models import User
import django.db.models.deletion 
# Create your models here.



class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete= models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']