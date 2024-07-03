from django.shortcuts import render

# Create your views here.

def Login(request):
    context = {}
    return render(request,'class/login.html',context)



def Student_signup(request):
    context = {}
    return render(request,"class/studentsignup.html",context)


def Teacher_signup(request):
    context = {}
    return render(request,"class/teachersignup.html",context)


def signup(request):
    return render(request,'class/signup.html')




