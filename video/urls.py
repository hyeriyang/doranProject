from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('genre/<int:genre>',views.search, name="search"),
    path('videolist/', views.videolist, name='videolist'),
    path('vdetail/<int:video_id>', views.vdetail, name='vdetail'),
    path('vcsave/<int:video_id>', views.vcsave, name='vcsave'),
    # 윤아 : 비디오 업로드
    path('vread/', views.vread, name="vread"),
    path('vcreate/', views.vcreate, name="vcreate"),
    path('vupdate/<int:pk>', views.vupdate, name="vupdate"),
    path('vdelete/<int:pk>', views.vdelete, name="vdelete"),
    path('<int:upload_id>/', views.udetail, name='udetail'),

]