from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView

from view_and_modify.myDB import getDb, getDbError

def modify_courses_page():
    win = Tk()
    win.title("Modify Contents Of Table : 'Courses'")
    win.geometry('1000x500+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'dark turquoise')

    return