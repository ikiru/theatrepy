# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    print 'Inside the the index method'
    return render(request,'frontend/main.html')

def about(request):
    print 'Inside the the about method'
    return render(request,'frontend/about.html')

def blog(request):
    pass
    print 'Inside the the blog method'
    return render(request,'frontend/blog.html')
