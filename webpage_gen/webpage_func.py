import os
import html
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import sqlite3


# Be sure to import our other modules
# so we can have access to them
import webpage_main
import webpage_gui



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
def save_statment(self):
    f = open("index.html", "w")
    html = """\
    <html>
      <head></head>
      <body>
        <p>
           <br><br><h1>{statement}</h1><br>
        </p>
      </body>
    </html>
    """.format(statement=statement)
    f.write(html)
    f.close()

    
    

# ====================================================================================
if __name__== '__main__':
    pass



    
    
                    
    
                
                
                










    

                    
