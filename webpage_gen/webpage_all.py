# Python Ver:   3.7.5
#
# Author:       Brian Reeves and Daniel A. Christie
#
# Purpose:      Wepage Demo. Demonstrating OOP, Tkinter GUI Module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import html
import sqlite3

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.statement = StringVar()

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,200) #(Height, Width)
        self.master.maxsize(500,200)
        self.master.title("Update Statement")
                            
        # This CenterWindow method will center our app on the user's screen
        center_window(self,500,200)
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalizd and clutter free
        load_gui(self)


        
def load_gui(self):
    # Blank Row
    self.lbl_space_1 = tk.Label(self.master,text='')
    self.lbl_space_1.grid(row=0,column=0,padx=(0,0),pady=(12,0),sticky=N+W)
    
    # Buttons
    self.btn_save = tk.Button(self.master,width = 13, height = 1, text='Save', command = lambda: retrieve_input(self))
    self.btn_save.grid(row=1,column=0,padx=(8,5),pady=(10,0),sticky=N+W)


    self.btn_close = Button(self.master,width = 13, height = 2, text="Close Program", command=lambda: ask_quit(self))
    self.btn_close.grid(row=3,column=1,padx=(8,5),pady=(10,0),sticky=N+E)
    
    # String Entry
    self.statement = tk.Entry(self.master, width=58, text='')
    self.statement.insert(END, 'Enter Statement')
    self.statement.grid(row=1, column=1, padx=(20,0), pady=(20,0))
    
def center_window(self, w, h): # pass in the tkniter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

# Open file
def retrieve_input(self):
    inputValue=self.statement.get()
    print(inputValue)
    f = open("index.html", "w")
    html = """\
    <html>
      <head></head>
      <body>
        <p>
           <br><br><h1> {inputValue} </h1><br>
        </p>
      </body>
    </html>
    """
    f.write(html)
    f.close()
        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
