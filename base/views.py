# coding=utf8
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/base/home.html')