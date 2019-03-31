from tkinter import *
from BooksAPI import search_by_title,search_by_ISBN,search_by_author
import time


def get_result():
    result.set("")
    start = time.time()
    query = entry_field.get()
    if var.get() == 1:
        result.set(search_by_title(query))
    if var.get() == 2:
        result.set(search_by_author(query))
    if var.get() == 3:
        result.set(search_by_ISBN(query))
    end = time.time()
    time1.set(end-start)


#COMPONENTS:
main = Tk(screenName = None,baseName = None,className = 'Book Search',useTk = 1)
entry_field = Entry(main)
time_label = Label(main,textvariable = time1)
r1 = Radiobutton(main,text = "Title",variable = var,value = 1)
r2 = Radiobutton(main,text = "Author",variable = var,value = 2)
r3 = Radiobutton(main,text = "ISBN",variable = var,value = 3)
search_button = Button(main,text = 'Search',activebackground = '#add8e6',command = get_result)
result_label = Label(main,textvariable = result)
main.state('zoomed')

#VARIABLES:
time1 = IntVar()
var = IntVar()
result = StringVar()

#PACKING:
entry_field.pack()
r1.pack()
r2.pack()
r3.pack()
search_button.pack()
result_label.pack()
time_label.pack()

#MAINLOOP
main.mainloop()
