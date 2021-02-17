from django.urls import include, path
from rest_framework.routers import DefaultRouter

from discussion import views

router = DefaultRouter()
router.register(r'topic', views.TopicViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
