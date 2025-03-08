from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.simpleIndex, name='simpleIndex'),
    path('<str:username>/', views.index, name='index'),
]
