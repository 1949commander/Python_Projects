# Python Ver:   3.8.3
#
# Author:       Brian Reeves
#
# Purpose:      File Move. Move TXT files that have been modified in the,
#                   last 24 hours.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame

# Be sure to import our other modules
# so we can have access to them
import file_move_gui
import file_move_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,200) #(Height, Width)
        self.master.maxsize(500,200)
        self.master.title("Check for files")
                            
        # This CenterWindow method will center our app on the user's screen
        file_move_func.center_window(self,500,200)
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_move_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalizd and clutter free
        file_move_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    path = ParentWindow()
