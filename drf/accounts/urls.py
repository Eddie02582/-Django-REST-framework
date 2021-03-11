
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, user_listview

#from extend import views
router = DefaultRouter()
router.register('user', UserViewSet)


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),	
    path('api/', include(router.urls)),    
    #path('user', TemplateView.as_view(template_name="user/listview.html"), name='user-listview'),
    path('user', user_listview, name='user-listview'),
    #path('proflie/', ProfileList.as_view()),
]

