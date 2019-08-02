from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('', views.bhome, name='bhome'),
    path('bwrite', views.bwrite, name='bwrite'),
    path('bdetail/<int:board_id>', views.bdetail, name='bdetail'),
    path('bhits/<int:board_id>', views.bhits, name='bhits'),
    path('bupdate/<int:board_id>', views.bupdate, name='bupdate'),
    path('bdelete/<int:board_id>', views.bdelete, name='bdelete'),
    
]