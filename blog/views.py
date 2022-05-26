from django.shortcuts import render
from django


def loginPage(request):

    context = {}
    return render(request, 'blog/login.html', context)
