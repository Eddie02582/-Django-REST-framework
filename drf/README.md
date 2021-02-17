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
```        


### �إ� API views  
�o�䦳�X�ؤ�k,�S���S�O�ݨD�����ϥ�ModelViewSet


#### CBV (APIView)

urls/py
```
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from discussion import views

urlpatterns = [
    path('topic/', views.TopicList.as_view()),
    path('topic/<int:pk>/', views.TopicDetail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
```
views.py
```
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Topic
from .serializers import TopicSerializer


class TopicList(APIView):
    """
    List all topics, or create a new topic.
    """
    def get(self, request, format = None):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class TopicDetail(APIView):
    """
    Retrieve, update or delete a topic instance.
    """
    def get_object(self, pk):
        try:
            return Topic.objects.get(pk = pk)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        topic = self.get_object(pk)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
    
#### GCBV (generic class-based views)
    
�ϥ�generic class-based views �i�H²��,�ô��ѧ�n��api�e��
    
```
from rest_framework import generics

from .models import Topic
from .serializers import TopicSerializer


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer   
```    

�p�G�u����Ū���i�H�ϥ�generics.ListAPIView�Mgenerics.RetrieveAPIView   
    
#### ModelViewSet    
```
from rest_framework import generics

from .models import Topic
from .serializers import TopicSerializer


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer   
```        
discussion/urls.py    
```
from django.urls import path
from rest_framework.routers import DefaultRouter

from discussion import views

router = DefaultRouter()
router.register(r'topic', views.TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

```   


    
    
    