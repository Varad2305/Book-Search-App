import requests
import json
import urllib
import cachetools
from functools import lru_cache

base_link = "https://www.googleapis.com/books/v1/volumes?q="
results_references = []
def search_by_title(query):
    link = base_link + query
    return generate_result(link)

def search_by_ISBN(query):
    link = base_link + "isbn:"+ query
    return generate_result(link)

def search_by_author(query):
    link = base_link + "inauthor:"+ query
    return generate_result(link)

def results_string(results_list):
    aux_result = ""
    for i in results_list:
        aux_result += "Title: " + i.title + "\n"
        author = ""
        for x in i.authors:
            author += x + " "
        aux_result += "Author(s): " + author + "\n"
        aux_result += "Preview Link: " + i.previewLink + "\n\n"
    return aux_result

@lru_cache(maxsize = 100)
def generate_result(link):
    response = requests.get(link).json()
    for x in response["items"]:
        title = x["volumeInfo"]["title"]
        authors = x["volumeInfo"]["authors"]
        previewLink = x["volumeInfo"]["previewLink"]
        b = Book(title,authors,previewLink)
        results_references.append(b)
    s = results_string(results_references)
    return s

class Book:
    def __init__(self,title,authors,previewLink):
        self.title = title
        self.authors = authors
        self.previewLink = previewLink
