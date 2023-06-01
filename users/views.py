from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            users = User.objects.get(username=username)
        except:
            messages.warning(request, "Username Doesn't exist")
            return redirect('login')

        users = authenticate(request, username=username, password=password)

        if users is not None:
            auth_login(request, users)
            return redirect('directory_view')
        else:
            messages.warning(request, "Username or password incorrect")
            return redirect('login')
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('directory_view')
