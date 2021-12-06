# Main page for the app.
from tkinter import *
import tkinter.messagebox as msb
from tkinter.ttk import Treeview
from PIL import Image, ImageTk

from myDB import getDb
from myDB import getDbError

# Main window.
root = Tk()                                     # Create main window.
root.geometry("750x600+0+0")                    # (width x height) + (shift_x) + (shift_y)
root.resizable(height = False, width = False)   # Disable resizing.
root.title("Ongoing Course Management System")  
root.config(bg = "dark goldenrod")              

# Create menu bar to view tables, commands not set yet.
Menu_Bar = Menu(root)
More_Menu = Menu(Menu_Bar, tearoff = 0)
More_Menu.add_command(label = 'Open Table \'Teachers\'', command = None)
More_Menu.add_separator()
More_Menu.add_command(label = 'Open Table \'Courses\'', command = None)
More_Menu.add_separator()
More_Menu.add_command(label = 'Open Table \'Clients\'', command = None)
More_Menu.add_separator()
More_Menu.add_command(label = 'Open Table \'Participants\'', command = None)
More_Menu.add_separator()
More_Menu.add_command(label = 'Open Table \'Course_History\'', command = None)
More_Menu.add_separator()
More_Menu.add_command(label = 'Quit', command = root.quit)
More_Menu.add_separator()
Menu_Bar.add_cascade(label = 'View Tables', menu = More_Menu)

# Widgets below.

# Run app.
if __name__ == '__main__':
    root.config(menu = Menu_Bar)
    root.mainloop()