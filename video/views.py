from django.shortcuts import render,get_object_or_404,redirect
import video.views
# 지연 
from .models import Video,VComment,Upload
# 윤아
from .forms import UploadForm

from django.utils import timezone
from datetime import datetime

from django.utils.dateformat import DateFormat

def search(request, genre):
    if genre=='bal':
        vs = Video.objects.filter(tags="발라드")
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

    

# 윤아
# 비디오 업로드 목록
def vread(request):
    uploads = Upload.objects.order_by('-id')
    return render(request, 'vread.html',{'uploads':uploads})

# 비디어 업로드 폼 생성
def vcreate(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
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