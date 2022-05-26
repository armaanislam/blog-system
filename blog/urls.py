from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('feed/', views.feedPage, name='feed'),
]