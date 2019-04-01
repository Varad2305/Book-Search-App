import tkinter as tk
from booksapi import search_by_title,search_by_ISBN,search_by_author,results_references,master_references,convert_to_string
import time

class MainApplication:
    def get_result(self):                               #Gets the result and sets it in the label that displays the result
        results_references.clear()
        start = time.time()
        query = self.entry_field.get()
        aux_result = ""
        if self.radio_var.get() == 1:
            self.txt.delete("1.0",tk.END)
            self.txt.insert(tk.INSERT,(search_by_title(query)))
        if self.radio_var.get() == 2:
            self.txt.delete("1.0",tk.END)
            self.txt.insert(tk.INSERT,(search_by_author(query)))
        if self.radio_var.get() == 3:
            self.txt.delete("1.0",tk.END)
            self.txt.insert(tk.INSERT,(search_by_ISBN(query)))
        end = time.time()
        self.timevar.set(end-start)

    def get_all_queries(self):                          #Used to display all the queries made by the user in that session
        self.txt.delete("1.0",tk.END)
        self.txt.insert(tk.INSERT,convert_to_string(master_references))

    def __init__(self,master):
        self.master = master
        self.txt_frm = tk.Frame(master,width = 600,height = 600)

        self.txt = tk.Text(self.txt_frm,borderwidth = 3,relief = "sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        self.scrollb = tk.Scrollbar(self.txt_frm,command = self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

        self.entry_field = tk.Entry(master)
        self.timevar = tk.IntVar()
        self.time_label = tk.Label(master,textvariable = self.timevar)

        self.radio_var = tk.IntVar()
        self.radio1 = tk.Radiobutton(master,text = "Title",variable = self.radio_var,value = 1)
        self.radio2 = tk.Radiobutton(master,text = "Author",variable = self.radio_var,value = 2)
        self.radio3 = tk.Radiobutton(master,text = "ISBN",variable = self.radio_var,value = 3)

        self.search_button = tk.Button(master,text = 'Search',activebackground = '#add8e6',command = self.get_result)

        self.all_queries = tk.Button(master,text = 'All Queries',activebackground = '#add8e6',command = self.get_all_queries)

        master.state("zoomed")

        self.entry_field.pack()

        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()

        self.search_button.pack()

        self.all_queries.pack()

        self.time_label.pack()

        self.txt_frm.pack(fill = "both",expand = "True")
        self.txt_frm.grid_propagate(False)
        self.txt_frm.grid_rowconfigure(0, weight=1)
        self.txt_frm.grid_columnconfigure(0, weight=1)

def main():
    main = tk.Tk(screenName = None,baseName = None,className = "Book Search",useTk = 1)
    app = MainApplication(main)
    main.mainloop()

if __name__ == '__main__':
    main()
