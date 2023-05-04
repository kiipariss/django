from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Home title',
        'num': [1, 2, 3, 4, 5, 6]
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
