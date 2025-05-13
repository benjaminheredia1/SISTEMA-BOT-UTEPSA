from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path ('AddMessage/', views.AddMessage),
    path('getCSRF', views.getCSRF)
]