from django.shortcuts import render,get_object_or_404,redirect
import video.views
# 지연 
from .models import Video,VComment
# 윤아
from .models import Upload
from .forms import UploadForm

from django.http import HttpResponse

from django.utils import timezone
from datetime import datetime
from django.utils.dateformat import DateFormat
from member.models import *

# 로그인 데코레이터
# from django.contrib.auth.decorators import login_required

## 코드 정리하기
def search(request, genre):
    if genre==1: # 랩/힙합
        vs = Video.objects.filter(tags="1")
    if genre==2: # 발라드
        vs = Video.objects.filter(tags="2")
    if genre==3: # POP
        vs = Video.objects.filter(tags="3")
    if genre==4: # 여름
        vs = Video.objects.filter(tags="4")
    if genre==5: # 밤/새벽
        vs = Video.objects.filter(tags="5")
    if genre==6: # 청량한
        vs = Video.objects.filter(tags="6")
    if genre==7: # 신나는
        vs = Video.objects.filter(tags="7")
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
    vlikes=video_detail.likes.count()
    if vlikes is None:
        vlikes="a"
  
    return render(request,'vdetail.html',{'video':video_detail,'vcomments':vcomments,'vlikes':vlikes})

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
def post_like(request, pk):
    video_detail=get_object_or_404(Video,pk=pk)
    if request.method=="POST":
        vcomment=VComment()
        vcomment.vpost=video_detail
        vcomment.author = request.POST['author']
        
        vcomment.text = request.POST['text']
        vcomment.save()

        vcomments=VComment.objects.filter(vpost=video_detail)
    # 포스트 정보 받아옴
    post = get_object_or_404(Video, pk=pk)

    # 사용자가 로그인 된건지 확인
    if not request.user.is_active:
        return redirect('vdetail',pk=pk, username=post.author, url=post.url)    

    # 사용자 정보 받아옴
    user = User.objects.get(username=request.user)
    # 좋아요에 사용자가 존재하면
    if post.likes.filter(id = user.id).exists():
        # 사용자를 지움
        post.likes.remove(user)
    else:
        # 아니면 사용자를 추가
        post.likes.add(user)
        
    # 포스트로 리디렉션
    return render(request,'vdetail.html',{'video':video_detail})
    #return redirect('vdetail',pk=pk, username=post.author, url=post.url)  

# 윤아
# 비디오 업로드 목록
def vread(request):
    uploads = Upload.objects.order_by('-id')
    return render(request, 'vread.html',{'uploads':uploads})

# 비디오 업로드 폼 생성
def vcreate(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.uname = request.user
            post.save()
            return redirect('vread')
    else:
        form = UploadForm()
        return render(request,'vcreate.html', {'form':form})

# 비디오 업로드 폼 수정
def vupdate(request, pk):
        upload = get_object_or_404(Upload, pk=pk)

        if request.method == "POST":
                form = UploadForm(request.POST, request.FILES, instance=upload) 

                if form.is_valid(): 
                        upload = form.save(commit=False) 
                        print(form.cleaned_data)
                        upload.utitle = form.cleaned_data['utitle']
                        upload.update_date=timezone.now()
                        blog.uname = request.user
                        upload.ubody = form.cleaned_data['ubody']
                        upload.uvideo = form.cleaned_data['uvideo'] 
                        upload.save()
                        return redirect('vread') 

        else:
                form = UploadForm(instance=upload) 
                return render(request, 'vupdate.html',{'form' : form})

# 비디오 업로드 삭제
def vdelete(request, pk):
    upload = Upload.objects.get(id=pk)
    upload.delete()
    return redirect('vread')
    
# 비디오 업르드 자세히
def udetail(request, upload_id):
    upload = get_object_or_404(Upload, pk=upload_id)
    return render(request,'udetail.html',{'upload':upload})

