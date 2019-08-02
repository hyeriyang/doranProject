from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('', views.test, name='test'),    
    #path('check', views.check, name='check'),
]