from django.shortcuts import render, redirect
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request,'index.html')
    # return render(request,'home.html')

def home(request):
    if request.user.is_anonymous:
        return redirect('/login') 
    return render(request, 'home.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request, 'home.html')
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid Credential!!")
    return render(request,'login.html')

def userCreate(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            password = password1
            user = User.objects.create_user(username, email, password)
            user.save()
            return render(request, 'home.html')
        else:
            messages.error(request, "Passwords didn't matched!!")
    return render(request, 'register.html')

def userLogout(request):
    logout(request)
    return redirect("/")