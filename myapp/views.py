from django.shortcuts import render
from requests.compat import quote_plus
import requests
from bs4 import BeautifulSoup

from . import models

BASE_URL = 'https://bulgaria.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    url = BASE_URL.format(quote_plus(search))
    response = requests.get(url)
    data = response.text
    
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'NaN'

        postings.append(
            (post_title,
            post_url,
            post_price
            )
        )

    context = {
        'search': search,
        'postings': postings
    }
    return render(request, 'myapp/new_search.html', context)