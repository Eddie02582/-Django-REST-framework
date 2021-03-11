from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Topic
from .serializers import TopicSerializer

# Create your views here.




@api_view(['GET', 'POST'])
def topic_list(request, format=None):
    """
    List all code topics, or create a new topic.
    """
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)   
    elif request.method == 'POST':
        serializer = TopicSerializer(data = request.data)       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
         return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data = request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
