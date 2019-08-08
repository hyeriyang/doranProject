from django.db import models
from django.contrib.auth.models import User
from video.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    # 지연 : 좋아요 test
    #like_posts = models.ManyToManyField('Video', blank=True, related_name='like_users')
    
    def __str__(self):
        return self.user.username
