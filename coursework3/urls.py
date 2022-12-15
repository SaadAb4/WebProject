from django.urls import path
from . import views
from coursework3.views import user_api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/user', user_api),
]