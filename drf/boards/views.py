from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Board, Post, Topic
from .serializers import BoardSerializer, PostSerializer, TopicSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer



class TopicViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    #需要傳額外參數
    def perform_create(self, serializer):   
        serializer.save(starter=self.request.user)


    @action(detail=False,methods=['get'])
    def query_board_topic(self,request):
        board = request.query_params.get('board',None)  
        reviews = Topic.objects.filter(board__name = board).order_by('-start_date')
        serializer = TopicSerializer(reviews,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    
    
def board_list(request):
    return render(request,"board/listview.html",{})


def topic_list(request,board_name):
    context = {}    
    context['board'] = Board.objects.get(name = board_name)
    return render(request,"topic/listview.html",context)
