from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    option = (
        ('draft','Draft'),('published','Published'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,unique_for_date='post_date')  
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_post')
    body = RichTextField(db_index=True)
    cat_desc = models.CharField(max_length=500)# short descriotion of category
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_app/images',default="")
  
    class Meta:
        ordering=('-post_date',)# ordering form 

    def __str__(self):
        return self.title + ' | ' + str(self.author)
     
    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return f"Comment by {self.name}"