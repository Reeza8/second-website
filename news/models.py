from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)        


class News(models.Model):
    image =models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category =models.ManyToManyField(Category) 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    date_hierarchy = 'pub_date'
    class Meta:
         ordering=['-published_date']
    def __str__(self):
            return self.title
    def get_absolute_url(self):
         return reverse('news:single',kwargs={'id':self.id})


# path('category/<str:category>',category,name='category'),
# path('category/date/<str:date>',category,name='category'),

class NewsLetter(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email