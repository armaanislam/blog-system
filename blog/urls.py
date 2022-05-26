from django.urls import path
from . import views

urlpatterns = [

    path('feed/', views.feedPage, name='feed'),

    #Login, Logout:
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    #User Profile (CRUD):
    path('register/', views.registerPage, name='register'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('update-user/', views.updateUser, name='update-user'),
    #path('delete-user/', views.deleteUser, name='delete-user'),

]