
from tkinter import *
from BooksAPI import search_by_title,search_by_ISBN,search_by_author

def get_result():
    query = entry_field.get()
    if var.get() == 1:
        result.set(search_by_title(query))
    if var.get() == 2:
        result.set(search_by_author(query))
    if var.get() == 3:
        result.set(search_by_ISBN(query))

main = Tk(screenName = None,baseName = None,className = 'Book Search',useTk = 1)
entry_field = Entry(main)
entry_field.pack()
var = IntVar()
r1 = Radiobutton(main,text = "Title",variable = var,value = 1)
r2 = Radiobutton(main,text = "Author",variable = var,value = 2)
r3 = Radiobutton(main,text = "ISBN",variable = var,value = 3)
r1.pack()
r2.pack()
r3.pack()
search_button = Button(main,text = 'Search',activebackground = '#add8e6',command = get_result)
search_button.pack()
result = StringVar()
result_label = Label(main,textvariable = result)
result_label.pack()
main.mainloop()
