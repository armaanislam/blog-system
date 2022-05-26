from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *


def loginUser(request):
    check = 'login'
    user = None
    username = None
    password = None

    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

    try:
        user = User.objects.filter(username=username)
    except:
        messages.error(request, 'User does not exists!')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('feed')
    else:
        messages.error(request, 'Username or password do not exist')

    context = {'check': check}
    return render(request, 'blog/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = UserCreationForm() #Form must be called before assigning request.POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.username.lower()
            user.save()
            #form.save()
            login(request, user)
            return redirect('feed')
            messages.success(request, 'Account has been created!')
    else:
        messages.error(request, 'Login failed.')
    context = {'form': form}
    return render(request, 'blog/login_register.html', context)


def feedPage(request):

    context = {}
    return render(request, 'blog/feed.html', context)

@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'blog/profile.html', context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)

    context = {'form': form}
    return render(request, 'blog/update-user.html', context)


#@login_required(login_url='login')
# def deleteUser(request):
#     user = request.user
#     form = UserForm(instance=user)
#
#     if request.method == "POST":
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#
#     context = {'form': form}
#     return render(request, 'blog/update-user.html', context)
