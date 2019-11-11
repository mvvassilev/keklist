from django.shortcuts import render
import requests

from bs4 import BeautifulSoup

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    context = {'search': search}
    return render(request, 'myapp/new_search.html', context)