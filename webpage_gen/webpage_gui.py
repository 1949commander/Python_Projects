from tkinter import *
import tkinter as tk


# Be sure to import our other modules
# so we can have access to them
import webpage_main
import webpage_func


def load_gui(self):
    # Blank Row
    self.lbl_space_1 = tk.Label(self.master,text='')
    self.lbl_space_1.grid(row=0,column=0,padx=(0,0),pady=(12,0),sticky=N+W)
    
    # Buttons
    self.btn_save = tk.Button(self.master,width = 13, height = 1, text='Save', command = lambda: webpage_func.save_statement(self))
    self.btn_save.grid(row=1,column=0,padx=(8,5),pady=(10,0),sticky=N+W)


    self.btn_close = Button(self.master,width = 13, height = 2, text="Close Program", command=lambda: webpage_func.ask_quit(self))
    self.btn_close.grid(row=3,column=1,padx=(8,5),pady=(10,0),sticky=N+E)
    
    # String Entry
    self.statement = tk.Entry(self.master, width=58, text='')
    self.statement.insert(END, 'Enter Statement')
    self.statement.grid(row=1, column=1, padx=(20,0), pady=(20,0))
    
    

    



if __name__ == "__main__":
    self.statement = StringVar()
    pass
