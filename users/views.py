from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserSignUpForm


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, 'Account created')
            return redirect('sign_in')
    else:
        form = UserSignUpForm()
    return render(request,"users/signup.html",{'form':form})


