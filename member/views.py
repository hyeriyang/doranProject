from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from .models import Profile
import json


def logout(request):
    auth.logout(request)
    return redirect('test')

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
                print("** function test (sign up) **")
                user = User.objects.create_user(
                    # user model fields
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password1"],
                )
                # one to one
                nickname = request.POST.get("nickname")
                print(type(nickname))
                profile = Profile(user=user, nickname=nickname)
                profile.save()
                auth.login(request,user)
                return redirect('test')
        return render(request, 'signup.html', {'error':'회원가입 실패 :: 중복된 아이디 혹은 닉네임'})
    return render(request, 'signup.html')

def user_exist(request):
    user = request.POST["username"]
    nickname = request.POST["nickname"]
    print("** function test (user_exist)**")
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
            return redirect('test')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')
