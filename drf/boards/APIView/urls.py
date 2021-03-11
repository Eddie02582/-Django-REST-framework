from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from discussion import views

# snippet_list = TopicList.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = TopicDetail.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


urlpatterns = [
    path('topic/', views.TopicList.as_view()),
    path('topic/<int:pk>/', views.TopicDetail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)


