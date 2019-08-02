from django.contrib import admin

# Register your models here.
# 지연
from .models import Video,VComment,Upload
admin.site.register(Video)
admin.site.register(VComment)
# 윤아
admin.site.register(Upload)