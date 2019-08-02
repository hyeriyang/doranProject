from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_date=models.DateField(null=True, blank=True)
    memo= models.CharField(max_length=200, blank=True)
    hits= models.IntegerField(null=True,blank=True)
    
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=True, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_thumbnail_url = models.TextField(max_length=300,default='')
    comment_textfield = models.TextField()

    def __str__(self):
        return self.comment_textfield