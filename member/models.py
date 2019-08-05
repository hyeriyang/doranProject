from django.db import models
from django.contrib.auth.models import User
from video.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)

    def __str__(self):
        return self.user.username
