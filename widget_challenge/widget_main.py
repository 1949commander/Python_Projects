# Python Ver:   3.7.5
#
# Author:       Brian Reeves and Daniel A. Christie
#
# Purpose:      Widget Demo. Demonstrating OOP, Tkinter GUI Module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Be sure to import our other modules
# so we can have access to them
import widget_gui
import widget_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,150) #(Height, Width)
        self.master.maxsize(500,150)
        self.master.title("Check for files")
                            
        # This CenterWindow method will center our app on the user's screen
        widget_func.center_window(self,500,150)
        self.master.protocol("WM_DELETE_WINDOW", lambda: widget_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalizd and clutter free
        widget_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    folder_path = StringVar()
    App = ParentWindow(root)
    root.mainloop()
