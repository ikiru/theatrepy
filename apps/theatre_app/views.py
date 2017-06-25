# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    print 'Inside the the index method'
    return render(request,'frontend/index.html')
