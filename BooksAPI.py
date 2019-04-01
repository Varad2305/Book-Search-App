import requests
import json
import urllib
import cachetools
from functools import lru_cache

base_link = "https://www.googleapis.com/books/v1/volumes?q="
results_references = []                                     #A temporary list to store the references of objects returned after 1 query
master_references = []                                      #A master list of references to store references to objects created by all queries

def search_by_title(query):
    link = base_link + query
    return generate_result(link)

def search_by_ISBN(query):
    link = base_link + "isbn:"+ query
    return generate_result(link)

def search_by_author(query):
    link = base_link + "inauthor:"+ query
    return generate_result(link)

def convert_to_string(results_list):                        #Takes information from a list of references to Book objects and places it into a string
    aux_result = ""
    for i in results_list:
        aux_result += "Title: " + i.title + "\n"
        aux_result += "Subtitle: " + i.subtitle + "\n"
        author = ""
        for x in i.authors:
            author += x + " "
        aux_result += "Author(s): " + author + "\n"
        aux_result += "Preview Link: " + i.previewLink + "\n\n"
    return aux_result

@lru_cache(maxsize = 100)                                   #Decorator to implement Least Recently Used cache
def generate_result(link):                                  #Uses the Google Books API to get data which then, uses to create objects. Stores references to these objects in 2 different lists mentioned above
    response = requests.get(link).json()
    for x in response["items"]:
        title = x["volumeInfo"]["title"]
        subtitle = x["volumeInfo"]["title"]
        authors = x["volumeInfo"]["authors"]
        previewLink = x["volumeInfo"]["previewLink"]
        b = Book(title,subtitle,authors,previewLink)
        results_references.append(b)
        master_references.append(b)
    return convert_to_string(results_references)


class Book:
    def __init__(self,title,subtitle,authors,previewLink):
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.previewLink = previewLink
