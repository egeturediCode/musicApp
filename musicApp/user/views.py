from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def Register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        messages.success(request,"Başarıyla kayıt oldunuz!")
        login(request,newUser)

        return redirect("index")


    content = {
        "form" : form
    }

    return render(request,"register.html",content)


def Login(request):
    form = LoginForm(request.POST or None)

    content = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            return render(request,"login.html",content)
        
        login(request,user)
        return redirect("index")
    

    return render(request,"login.html",content)

def Logout(request):
    logout(request)

    return redirect("index")
