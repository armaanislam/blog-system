from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *



def loginPage(request):

    context = {}
    return render(request, 'blog/login.html', context)

def registerPage(request):

    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        message.success(request, 'Account has been created!')
    context = {}
    return render(request, 'blog/register.html', context)