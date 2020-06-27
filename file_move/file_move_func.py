from tkinter import *
import os
from tkinter import filedialog
import tkinter as tk
import sqlite3
import glob
import datetime
from datetime import timedelta
import shutil
from tkinter import messagebox
# Be sure to import our other modules
# so we can have access to them
import file_move_main
import file_move_gui

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
    originPath = filedialog.askdirectory()
    self.folder_orig.insert(0, originPath)
    print(originPath)

# Open file
def dest_button(self):
    # Allow user to select a directory and store it in var
    # called folder_dest
    destinationPath = filedialog.askdirectory()
    self.folder_dest.insert(0,destinationPath)
    print(destinationPath)

    
# Find files
def get_file_list(self):
    # Select Origin Folder
    self.originPath = self.folder_orig.get()
    # Select Destination Folder
    self.destinationPath = self.folder_dest.get()
    # Create a list of files in the Origin Folder
    source_files = os.listdir(self.originPath)
    # Determine files to be moved, Requirements:
    # Move only .TXT files modified within last 24 hours
    for file in source_files:
        abs_file_path = os.path.join(self.originPath, file)
        modifyDate = os.path.getmtime(abs_file_path)
        todaysDate = datetime.datetime.now()- timedelta(hours=24)
        date_time_file =  datetime.datetime.fromtimestamp(modifyDate)
        if file.endswith("txt")and todaysDate < date_time_file:
            shutil.move(self.originPath +'/'+ file, self.destinationPath)
            print(file)


          
#===================================================================================
if __name__== '__main__':
    pass



    
    
                    
    
                
                
                










    

                    
