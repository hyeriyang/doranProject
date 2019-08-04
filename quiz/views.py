from django.shortcuts import render

# Create your views here.

def quiz(request):
    return render(request, 'quiz.html')   
