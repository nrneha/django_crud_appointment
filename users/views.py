from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserSignUpForm
from. models import *
from django.contrib.auth import authenticate, login
from booking import urls


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created')
            return redirect('sign_in')
    else:
        form = UserSignUpForm()
    return render(request,"users/signup.html",{'form':form})



def sign_in(request):
    return render(request,"users/signin.html")


def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
    return redirect("users:signup")

    
        



