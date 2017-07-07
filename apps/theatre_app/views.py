# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ProfileForm
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def profile_create(request):
    form = ProfileForm()
    context = {
        "form": form
    }
    return render(request, 'profile/user_profile.html', context)


def index(request):
    print 'Inside the the index method'
    return render(request, 'frontend/main.html')


def about(request):
    print 'Inside the the about method'
    return render(request, 'frontend/about.html')


def profile(request):
    pass
    print 'Inside the the blog method'
    return render(request, 'profile/user_profile.html')


def login(request):

    return render(request, 'profile/login.html')


def register(request):

    return render(request, 'profile/register.html')
