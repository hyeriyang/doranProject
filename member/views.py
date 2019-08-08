from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from .models import Profile
from video.models import Video
import json

def mypage(request):
    video=Video.objects.all()
    polldict={}
    user=request.user
    real=[]
    for poll in Video.objects.all():
        index=poll.title
        choicedict={}
        
        choicedict[index] = poll.likes.all()
        sedex=0
        for x in choicedict[index]:
            if x==user:
                real.append(index)

        polldict[index]=choicedict
        #print(polldict[index])

    # real이 진짜 좋아요를 누른 영상들
    # video객체를 가져 오겠다
    like_videos=[]
    for y in real:
        #like_videos.append(Video.objects.filter(title=y).values('video_key'))
        like_videos.append(Video.objects.filter(title=y))

    yyy=[]
    for ob in like_videos:
        for o in ob:
            for vo in video:
                if vo.title==o:
                    yyy.append(vo)
                else:
                    yyy.append(o)
    yyy = list(set(yyy))                

        #obs=Video.objects.filter(title=ob)
    #like_videos = Video.objects.filter(title="1")

    return render(request, 'mypage.html',{'video':video,
                                            'yyy':yyy,
                                            'real':real,
                                            'like_videos':like_videos
                                        })



def edit(request, pk): # 개인정보 수정
    if request.method=="POST":
        if request.POST["password1"]==request.POST["password2"]:
            user = User.objects.get(id=pk)
            user.email=request.POST["email"]
            user.password=request.POST["password1"]
            
            profile=Profile.objects.get(user_id=pk)
            profile.nickname=request.POST["nickname"]
            user.save()
            profile.save()
            auth.login(request,user)
            return redirect('main')
            
    return render(request, 'edit.html')

def logout(request):
    auth.logout(request)
    return redirect('main')

def signup(request):
    if request.method=="POST":
        if request.POST["password1"]==request.POST["password2"]:
            if user_exist(request)==True:
                return render(request, 'signup.html', {'error1':'존재하는 아이디'})
            elif email_exist(request)==True:
                return render(request, 'signup.html', {'error2':'존재하는 이메일'})
            elif nick_exist(request)==True:
                return render(request, 'signup.html', {'error3':'존재하는 닉네임'})
            else:
                #print("** function test (sign up) **")
                user = User.objects.create_user(
                    # user model fields
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password1"],
                )
                # one to one
                nickname = request.POST.get("nickname")
                #print(type(nickname))
                profile = Profile(user=user, nickname=nickname)
                profile.save()
                auth.login(request,user)
                return redirect('main')
        return render(request, 'signup.html', {'error':'회원가입 실패 :: 중복된 아이디 혹은 닉네임'})
    return render(request, 'signup.html')

def user_exist(request):
    user = request.POST["username"]
    nickname = request.POST["nickname"]
    #print("** function test (user_exist)**")
    if User.objects.filter(username=user).exists():
        return True
    else:
        return False

def email_exist(request):
    email = request.POST["email"]
    if User.objects.filter(email=email).exists():
        return True
    else: 
        return False

def nick_exist(request):
    nickname=request.POST["nickname"]
    if Profile.objects.filter(nickname=nickname).exists():
        return True
    else:
        return False

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')
