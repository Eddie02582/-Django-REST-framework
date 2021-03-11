from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from discussion import views

urlpatterns = [
    path('topic/', views.topic_list),
    path('topic/<int:pk>/', views.topic_detail),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
