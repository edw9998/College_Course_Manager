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

    # Frame for entries.
    courses_frame = Frame(win, bd = 5, height = 450, width = 400, bg = 'dark turquoise', relief = GROOVE)
    courses_frame.place(x = 0, y = 50)

    '''
    Label & entry for column 'course_id'.
    Label Y - Interval = 50.0 px Incrementation.
    Label to Entry Distance = 175.0 px. 
    '''
    course_id_label = Label(courses_frame, text = 'Course - ID(PK)', font = ('Times New Roman', 15),
                                           fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    course_id_entry = Entry(courses_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                           fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    course_id_label.place(x = 0, y = 0)
    course_id_entry.place(x = 175, y = 0)

    '''
    Label & entry for column 'course_name'.
    '''
    course_name_label = Label(courses_frame, text = 'Course Name', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    course_name_entry = Entry(courses_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    course_name_label.place(x = 0, y = 0 + 50)
    course_name_entry.place(x = 175, y = 0 + 50)

    '''
    Label & entry for column 'final_score'.
    '''

    return