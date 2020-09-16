from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models

import requests

BASE_CRAIGSLIST_URL = 'https://bangalore.craigslist.org/search/bbb?query={}'


def index(request):
    return render(request, 'my_app/index.html', {})

def new_search(request):
    
    search = request.POST.get('search')
    models.Search.objects.create(search = search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    post_titles = soup.find_all('a', {'class' : 'result-title'})
   # print(post_titles[0].text)
    

    stuff_for_frontend = {
        'search' : search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)

















