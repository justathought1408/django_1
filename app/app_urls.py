from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('posts/', posts, name='posts'),
    path('posts/article/<slug:id_slug>/', article, name='article'),
    path('posts/vacancies/<slug:id_slug_vac>/', vacancies, name='vacancy'),
]