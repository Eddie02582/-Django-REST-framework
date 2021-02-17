# Django-REST-framework
 Django REST framework

## �w��

�R�O���ܦr�� (cmd ) ���U��J
```
    pip install django
    pip install djangorestframework
```

## �إ߱M��
```
    django-admin startproject drf
```

�bdrf/drf/settings.py ��INSTALLED_APPS �s�Wrest_framework

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

## �إ�App
�bdrf �R�O���ܦr�� (cmd )���U��J
```
    django-admin startapp discussion
```

�bdrf/drf/settings.py ��INSTALLED_APPS �s�Wrest_framework

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
### �إ�model


�bdiscussion/models �s�W�H�U
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



   
�b�R�O���ܦr�� (cmd )���U��J
```
    python manage.py makemigrations
```  
�b�R�O���ܦr�� (cmd )���U��J  
```
    python manage.py migrate
```       

### �إ� Serializer class


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

### �إ� API views  
�S���S�O�ݨD�����ϥ�ModelViewSet,��L��k�b�O�g�Բӻ���
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

RestAPI ²��N�����F


<img scr = "https://github.com/Eddie02582/Django-REST-framework/blob/main/Quick%20Start/viewset-1.png">

<img scr = "https://github.com/Eddie02582/Django-REST-framework/blob/main/Quick%20Start/viewset-2.png">









    
    
    