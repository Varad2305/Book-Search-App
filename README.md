# Book-Search-App
An Application which uses the Google Books API to let the user search for books using the Title, Author or ISBN number. 

# How to Use
1.Enter your query in the text field at the top of the window\
2.Select whether you want to search by Title, Author or ISBN number\
3.Hit Search to get all the results\
4.The time required to execute the query is displayed below the 'All Queries' button\
5.You can click the 'All Queries' button to view results of all the queries you made until that point

# Installation
## You'll need the following technologies:
1.Python 3

## You'll need the following python libraries:
1.requests\
2.json\
3.urllib\
4.functools\
5.tkinter\
6.time

## Steps:
1.Navigate to the folder 'BookProject'\
2.Run the command 'python MainApp.py'

# Features:
## 1. Google Books API: 
This program uses the Google Books API to search for books
## 2. LRU cache: 
The application uses 'Least Recently Used' cache to temporarily store results of queries to improve performance
## 3. All Queries button:
The user can click on the 'All Queries' button to see all the queries made until that point of time
## 4.Time Label:
The time taken to execute the query is displayed below the 'All Queries' button

# Notes
1. The data taken from the Google Books API is not always consistent. If a query does not work even if there is a book like that, it must be because the program is trying to access some information which is not there in the data received. The program is trying to access data which is most commonly available.
