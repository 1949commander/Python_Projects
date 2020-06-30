from tkinter import *
import tkinter as tk


# Be sure to import our other modules
# so we can have access to them
import widget_main
import widget_func


def load_gui(self):
    # Blank Row
    self.lbl_space_1 = tk.Label(self.master,text='')
    self.lbl_space_1.grid(row=0,column=0,padx=(0,0),pady=(12,0),sticky=N+W)
    
    # Buttons
    self.btn_brow = tk.Button(self.master,width = 13, height = 1, text='Browse...', command = lambda: widget_func.browse_button(self))
    self.btn_brow.grid(row=1,column=0,padx=(8,5),pady=(10,0),sticky=N+W)

    self.btn_dest = tk.Button(self.master,width = 13, height = 1, text='Browse...', command = lambda: widget_func.dest_button(self))
    self.btn_dest.grid(row=2,column=0,padx=(8,5),pady=(10,0),sticky=N+W)

    self.btn_check = Button(self.master, text="Check for files...", width = 13, height = 2)
    self.btn_check.grid(row=3,column=0,padx=(8,5),pady=(10,0),sticky=N+W)

    self.btn_close = Button(self.master,width = 13, height = 2, text="Close Program", command=lambda: widget_func.ask_quit(self))
    self.btn_close.grid(row=3,column=1,padx=(8,5),pady=(10,0),sticky=N+E)
    
    # String Entry
    self.folder_path = tk.Entry(self.master, width=58, text='')
    self.folder_path.insert(END, 'File Directory')
    self.folder_path.grid(row=1, column=1, padx=(20,0), pady=(20,0))
    
    self.folder_dest = tk.Entry(self.master, width=58, text='')
    self.folder_dest.insert(END, 'Destination Directory')
    self.folder_dest.grid(row=2, column=1, padx=(20,0), pady=(20,0))
    

    



if __name__ == "__main__":
    # self.folder_path = StringVar()
    # self.folder_dest = StringVar()
    pass
