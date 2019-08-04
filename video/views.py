from django.shortcuts import render,get_object_or_404,redirect
import video.views
# 지연 
from .models import Video,VComment 
from django.utils import timezone
from datetime import datetime

from django.utils.dateformat import DateFormat

## 코드 정리하기
def search(request, genre):
    if genre=='bal':
        vs = Video.objects.filter(tags="발라드")
    if genre=='hip':
        vs = Video.obejcsts.filter(tags="랩/힙합")
    if gnere=='fresh':
        vs = Video.obejcsts.filter(tags="청량한")
    if genre=='fun':
        vs = Video.obejcsts.filter(tags="신나는")
    return render(request,'videolist.html', {'vs':vs})


# 지연 : 비디오 재생 페이지를 로드
def videolist(request):
    videos=Video.objects 
    return render(request,'videolist.html',{'videos':videos})

# 지연 : 비디오 한개 보여주는 페이지 로드
def vdetail(request,video_id):
    videos=Video.objects 
    
    
    video_detail=get_object_or_404(Video,pk=video_id)
    vcomments=VComment.objects.filter(vpost=video_detail)
    return render(request,'vdetail.html',{'video':video_detail,'vcomments':vcomments})

# 지연 : 댓글 저장 기능만 하는 함수
def vcsave(request,video_id):
    videos=Video.objects
    video_detail=get_object_or_404(Video,pk=video_id)
    if request.method=="POST":
        vcomment=VComment()
        vcomment.vpost=video_detail
        vcomment.author = request.POST['author']
        
        vcomment.text = request.POST['text']
        vcomment.save()

        vcomments=VComment.objects.filter(vpost=video_detail)
        return render(request,'vdetail.html',{'video':video_detail,'vcomments':vcomments})
        #return redirect('/video/vdetail',pk=video_id)
    else:
        return render(request, 'comment.html', {'form': form})

    
     