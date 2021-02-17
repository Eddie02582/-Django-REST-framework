# Django-REST-framework
 Django REST framework

## 安裝

命令提示字元 (cmd ) 底下輸入
```
    pip install django
    pip install djangorestframework
```

## 建立專案
```
    django-admin startproject drf
```

在drf/drf/settings.py 的INSTALLED_APPS 新增rest_framework

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
```

## 建立App
在drf 命令提示字元 (cmd )底下輸入
```
    django-admin startapp discussion
```

在drf/drf/settings.py 的INSTALLED_APPS 新增rest_framework

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'discussion'
]
```
### 建立model


在discussion/models 新增以下
```
from django.contrib.auth.models import User
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)    
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject		

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now = True)
``` 



   
在命令提示字元 (cmd )底下輸入
```
    python manage.py makemigrations
```  
在命令提示字元 (cmd )底下輸入  
```
    python manage.py migrate
```       

### 建立 Serializer class


#### Use serializers.Serializer
    
    
    
    
#### Use serializers.ModelSerializer    
discussion/serializers.py
```
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views']
      

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'topic']

```  

### 建立 API views  
沒有特別需求直接使用ModelViewSet,其他方法在別篇詳細說明
ModelViewSet    
```
from rest_framework import viewsets

from .models import Post, Topic
from .serializers import PostSerializer, TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

```        
discussion/urls.py    
```
from django.urls import path
from rest_framework.routers import DefaultRouter

from discussion import views

router = DefaultRouter()
router.register(r'topic', views.TopicViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```  

RestAPI 簡單就完成了


<img scr = "https://github.com/Eddie02582/Django-REST-framework/blob/main/Quick%20Start/viewset-1.png">

<img scr = "https://github.com/Eddie02582/Django-REST-framework/blob/main/Quick%20Start/viewset-2.png">









    
    
    