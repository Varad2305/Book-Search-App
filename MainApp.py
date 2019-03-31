from tkinter import *
from BooksAPI import search_by_title,search_by_ISBN,search_by_author,results_references,master_references,convert_to_string
import time
import copy
import webbrowser

def get_result():                               #Gets the result and sets it in the label that displays the result
    results_references.clear()
    start = time.time()
    query = entry_field.get()
    aux_result = ""
    if radio_var.get() == 1:
        txt.delete("1.0",END)
        txt.insert(INSERT,(search_by_title(query)))
    if radio_var.get() == 2:
        txt.delete("1.0",END)
        txt.insert(INSERT,(search_by_author(query)))
    if radio_var.get() == 3:
        txt.delete("1.0",END)
        txt.insert(INSERT,(search_by_ISBN(query)))
    end = time.time()
    time1.set(end-start)

def get_all_queries():                          #Used to display all the queries made by the user in that session
    txt.delete("1.0",END)
    txt.insert(INSERT,convert_to_string(master_references))

#COMPONENTS:
main = Tk(screenName = None,baseName = None,className = "Book Search",useTk = 1)
txt_frm = Frame(main,width = 600,height = 600)
txt = Text(txt_frm,borderwidth = 3,relief = "sunken")
txt.config(font=("consolas", 12), undo=True, wrap='word')
txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
scrollb = Scrollbar(txt_frm,command = txt.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
txt['yscrollcommand'] = scrollb.set
entry_field = Entry(main)
time1 = IntVar()
time_label = Label(main,textvariable = time1)
radio_var = IntVar()
r1 = Radiobutton(main,text = "Title",variable = radio_var,value = 1)
r2 = Radiobutton(main,text = "Author",variable = radio_var,value = 2)
r3 = Radiobutton(main,text = "ISBN",variable = radio_var,value = 3)
search_button = Button(main,text = 'Search',activebackground = '#add8e6',command = get_result)
all_queries = Button(main,text = 'All Queries',activebackground = '#add8e6',command = get_all_queries)
main.state('zoomed')

#PACKING:
entry_field.pack()
r1.pack()
r2.pack()
r3.pack()
search_button.pack()
all_queries.pack()
time_label.pack()
txt_frm.pack(fill = "both",expand = "True")
txt_frm.grid_propagate(False)
txt_frm.grid_rowconfigure(0, weight=1)
txt_frm.grid_columnconfigure(0, weight=1)

#MAINLOOP
main.mainloop()
