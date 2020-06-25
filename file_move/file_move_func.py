import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import sqlite3
import glob
import datetime
import shutil

# Be sure to import our other modules
# so we can have access to them
import file_move_main
import file_move_gui

originPath = ('')
destinationPath = ('')
fileType = ".txt"

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
    self.folder_path.insert(0, originPath)
    print(originPath)

# Open file
def dest_button(self):
    # Allow user to select a directory and store it in var
    # called folder_dest
    destinationPath = filedialog.askdirectory()
    self.folder_dest.insert(0,destinationPath)
    print(destinationPath)

    
# Move files
def get_file_list(self):
    self.path = originPath
    self.type = fileType
    '''
    Return a list of filename matching the given path and file type
    '''
    return glob.glob(self.path + "*" + self.type)

##    # Create list of text filenames in Origin folder
##    self.fileList = get_file_list(self.originPath, self.fileType)
##    for file in fileList:
##    # Get last modified date and today's date
##        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
##        todaysDate = datetime.datetime.today()
##    
##    filePathList = file.split("\\") # Create a list from the filepath
##    filename = filePathList[-1] # The last element is a the filename
##    
##    # If modified within last 24 hours, then copy to destination folder
##    modifyDateLimit = modifyDate + datetime.timedelta(days=1)
##
##    # If the file was edited less then 24 hours ago then copy it
##    if modifyDateLimit > todaysDate:
##        shutil.copy2(file, destinationPath + filename)    

# ====================================================================================
if __name__== '__main__':
    pass



    
    
                    
    
                
                
                










    

                    
