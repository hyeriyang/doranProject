from django.contrib import admin
from django.urls import path, include
# import user.views
# import video.views # 지연
import board.views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',board.views.home,name='home'),
   # path('user/', include('user.urls')),
   # path('video/', include('video.urls')),
    path('board/', include('board.urls')),

]