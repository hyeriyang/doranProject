from django.contrib import admin
from django.urls import path, include
# import user.views
# import video.views # 지연
import board.views
import quiz.views
import main.views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.main,name='main'),
    path('user/', include('member.urls')),
    path('video/', include('video.urls')),
    path('board/', include('board.urls')),
    path('quiz/', include('quiz.urls')),
    path('main/', include('main.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)