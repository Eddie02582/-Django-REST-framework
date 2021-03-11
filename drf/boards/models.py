# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)    
    def __str__(self):
        return self.name
        
    def get_posts_count(self):        
        return Post.objects.filter(topic__board=self).count()
        
    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

    def get_topics_count(self):
        return self.topics.count()
        

class Topic(models.Model):
    subject = models.CharField(max_length=255) 
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE)  
    description = models.TextField(max_length = 2000,default = "")    
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject	

    def get_post_count(self):
        return self.posts.count()        

    def get_last_post(self, obj):
        return Post.objects.filter(topic =self).order_by('-created_at').first()


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.message
