from django.urls import path
from . import views
from coursework3.views import user_api, items_api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/user', user_api),
    path('api/items/', items_api),
    path('login_user', views.login_user, name='login'),
    
]