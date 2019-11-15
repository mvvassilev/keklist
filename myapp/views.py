from django.shortcuts import render
from requests.compat import quote_plus
import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://berlin.craigslist.org/search/hhh?query={}'

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    # response = requests.get('https://berlin.craigslist.org/search/sss?query=asdgasdasdd')
    # data = response.text
    # print(data)
    context = {'search': search}
    return render(request, 'myapp/new_search.html', context)