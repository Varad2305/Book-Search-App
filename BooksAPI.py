import requests
import json
import urllib
import cachetools
import time
from cachetools import cached,TTLCache
cache = TTLCache(maxsize = 100, ttl = 300)

@cached(cache)
def search_by_title(query):
    link = "https://www.googleapis.com/books/v1/volumes?q="+query
    return generate_result(link)

@cached(cache)
def search_by_ISBN(query):
    link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+query
    return generate_result(link)

@cached(cache)
def search_by_author(query):
    link = "https://www.googleapis.com/books/v1/volumes?q=inauthor:"+query
    return generate_result(link)

def generate_result(link):
    response = requests.get(link).json()
    final_result = ''
    for x in response["items"]:
        final_result += x["volumeInfo"]["title"] + " by "
        for i in x["volumeInfo"]["authors"]:
            final_result += i + ", "
        final_result += '\n\n'
    return final_result

