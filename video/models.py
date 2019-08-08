# 지연
from django.db import models
from django.utils import timezone
# title / date / video / body / link : video는 뭐쥬?
# user 연결
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200) # 영상 제목
    body = models.TextField() # 영상 내용
    author = models.CharField(max_length=200,null=True) #영상 게시자
    date = models.DateTimeField(auto_now=True) # 게시 날짜
    video_key=models.CharField(max_length=50, null=True) # 비디오 링크
    tags = models.CharField(max_length=300, null=True) # 장르 및 태그 

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]

class VComment(models.Model):
    vpost = models.ForeignKey(Video,on_delete=models.PROTECT) # 어느 게시물과 연관있는가
    author = models.CharField(max_length=200) #작성자
    text = models.TextField() # 댓글내용
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) # ??

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()

# 윤아
class Upload(models.Model):
    utitle = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    uname = models.CharField(max_length=30, blank=True)
    ubody = models.TextField()
    uvideo = models.FileField(upload_to="uploads/%Y/%m/%d", null=True)

    def __str__(self):
        return self.utitle