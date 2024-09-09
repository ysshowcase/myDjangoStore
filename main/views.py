from typing import Dict

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home page - Django Store',
        'content': 'Sample Dj Store'

    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("About")
    context = {
        'title': 'About page - Django Store',
        'content': 'About page',
        'text_on_page': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit'
    }
    return render(request, 'main/about.html', context)
