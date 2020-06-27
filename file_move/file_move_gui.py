
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import Frame


# Be sure to import our other modules
# so we can have access to them
import file_move_main
import file_move_func


def load_gui(self):
    # Blank Row
    self.lbl_space_1 = tk.Label(self.master,text='')
    self.lbl_space_1.grid(row=0,column=0,padx=(0,0),pady=(0,0),sticky=N+W)
    
    # Buttons
    self.btn_brow = tk.Button(self.master,width = 13, height = 1, text='Browse...', command = lambda: file_move_func.browse_button(self))
    self.btn_brow.grid(row=0,column=0,padx=(10,5),pady=(20,0),sticky=W)

    self.lbl_type = tk.Label(self.master,width = 13, height = 2, text='File \nExtension')
    self.lbl_type.grid(row=1,column=0,padx=(10,5),pady=(10,0),sticky=W)

    self.btn_dest = tk.Button(self.master,width = 13, height = 1, text='Browse...', command = lambda: file_move_func.dest_button(self))
    self.btn_dest.grid(row=2,column=0,padx=(10,5),pady=(20,0),sticky=W)

    self.btn_check = Button(self.master,width = 13, height = 2, text="Move files...", command = lambda: file_move_func.get_file_list(self))
    self.btn_check.grid(row=3,column=0,padx=(10,5),pady=(10,0),sticky=W)

    self.btn_close = Button(self.master,width = 13, height = 2, text="Close Program", command = lambda: file_move_func.ask_quit(self))
    self.btn_close.grid(row=3,column=1,padx=(0,60),pady=(10,0),sticky=E)
    
    # String Entry
    self.folder_orig = tk.Entry(self.master, width=60, text='')
    self.folder_orig.insert(END, '')
    self.folder_orig.grid(row=0, column=1, padx=(10,0), pady=(20,0), sticky=W)

    self.file_type = tk.Label(self.master, width=60, anchor=W, text='*.txt')
    self.file_type.grid(row=1, column=1, padx=(10,0), pady=(15,0), sticky=W)
  
    self.folder_dest = tk.Entry(self.master, width=60, text='')
    self.folder_dest.insert(END, '')
    self.folder_dest.grid(row=2, column=1, padx=(10,0), pady=(20,0), sticky=W)
    

    



if __name__ == "__main__":
    pass
