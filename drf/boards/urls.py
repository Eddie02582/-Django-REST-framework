from django.urls import include, path
from rest_framework.routers import DefaultRouter

from boards import views

router = DefaultRouter()
router.register('board', views.BoardViewSet)
router.register('topic', views.TopicViewSet)
router.register('post', views.PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.board_list,name='board-listview'), 
    path('<str:board_name>/', views.topic_list,name='board_topics'), 
]
