from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('videolist/', views.videolist, name='videolist'),
    path('vdetail/<int:video_id>', views.vdetail, name='vdetail'),
    path('vcsave/<int:video_id>', views.vcsave, name='vcsave'),
    
]