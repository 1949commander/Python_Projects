import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import sqlite3


# Be sure to import our other modules
# so we can have access to them
import widget_main
import widget_gui



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
def browse_button(self):
    # Allow user to select a directory and store it in var
    # called folder_path
    filename1 = filedialog.askdirectory()
    self.folder_path.insert(0, filename1)

# Open file
def dest_button(self):
    # Allow user to select a directory and store it in var
    # called folder_path
    filename2 = filedialog.askdirectory()
    self.folder_dest.insert(0,filename2)
    
    

# ====================================================================================
if __name__== '__main__':
    pass



    
    
                    
    
                
                
                










    

                    
