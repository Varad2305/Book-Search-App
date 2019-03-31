from tkinter import *
from BooksAPI import search_by_title,search_by_ISBN,search_by_author,results_references,master_references,convert_to_string
import time
import copy

def get_result():                               #Gets the result and sets it in the label that displays the result
    results_references.clear()
    start = time.time()
    query = entry_field.get()
    res.set("")
    aux_result = ""
    if radio_var.get() == 1:
        res.set(search_by_title(query))
    if radio_var.get() == 2:
        res.set(search_by_author(query))
    if radio_var.get() == 3:
        res.set(search_by_ISBN(query))
    end = time.time()
    time1.set(end-start)

def get_all_queries():                          #Used to display all the queries made by the user in that session
    res.set(convert_to_string(master_references))

#COMPONENTS:
main = Tk(screenName = None,baseName = None,className = "Book Search",useTk = 1)
entry_field = Entry(main)
time1 = IntVar()
time_label = Label(main,textvariable = time1)
radio_var = IntVar()
r1 = Radiobutton(main,text = "Title",variable = radio_var,value = 1)
r2 = Radiobutton(main,text = "Author",variable = radio_var,value = 2)
r3 = Radiobutton(main,text = "ISBN",variable = radio_var,value = 3)
search_button = Button(main,text = 'Search',activebackground = '#add8e6',command = get_result)
all_queries = Button(main,text = 'All Queries',activebackground = '#add8e6',command = get_all_queries)
res = StringVar()
result_label = Label(main,textvariable = res,justify = LEFT)
main.state('zoomed')

#PACKING:
entry_field.pack()
r1.pack()
r2.pack()
r3.pack()
search_button.pack()
all_queries.pack()
time_label.pack()
result_label.pack(side = LEFT,fill = BOTH)

#MAINLOOP
main.mainloop()
