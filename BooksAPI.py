import requests
import json
import urllib
import cachetools
import time
from functools import lru_cache

@lru_cache(maxsize = 100)
def search_by_title(query):
    link = "https://www.googleapis.com/books/v1/volumes?q="+query
    return generate_result(link)

@lru_cache(maxsize = 100)
def search_by_ISBN(query):
    link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+query
    return generate_result(link)

@lru_cache(maxsize = 100)
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
