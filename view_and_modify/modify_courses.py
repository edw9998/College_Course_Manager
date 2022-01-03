from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView

from view_and_modify.myDB import getDb, getDbError

def modify_courses_page():
    win = Tk()
    win.title("Modify Contents Of Table : 'Courses'")
    win.geometry('1000x390+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'dark turquoise')

    # Title for frame.
    courses_frame_title = Label(win, text = 'COURSE DETAILS', font = ("Times New Roman", 15, "bold"),
                                       bg = 'dark turquoise', fg = 'red', width = 20, justify = CENTER)
    courses_frame_title.place(x = 75, y = 25)

    # Frame for entries.
    courses_frame = Frame(win, bd = 5, height = 341, width = 393, bg = 'dark turquoise', relief = GROOVE)
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
    final_score_label = Label(courses_frame, text = 'Final Score', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    final_score_entry = Entry(courses_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    final_score_label.place(x = 0, y = 0 + 100)
    final_score_entry.place(x = 175, y = 0 + 100)

    '''
    Label & entry for column 'level'.
    '''
    level_label = Label(courses_frame, text = 'Level', font = ('Times New Roman', 15),
                                         fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    level_entry = Entry(courses_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                       fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    level_label.place(x = 0, y = 0 + 150)
    level_entry.place(x = 175, y = 0 + 150)

    '''
    Label & entry for column 'course_price(US$)'.
    '''
    course_price_label = Label(courses_frame, text = 'Course Price(US$)', font = ('Times New Roman', 15),
                                                fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    course_price_entry = Entry(courses_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                              fg = 'black', justify = LEFT, relief = GROOVE, width = 20)      
    course_price_label.place(x = 0, y = 0 + 200)
    course_price_entry.place(x = 175, y = 0 + 200)

    '''
    Label & entry for column 'start_date'.
    '''    
    start_date_label = Label(courses_frame, text = 'Start Date', font = ('Times New Roman', 15),
                                              fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    start_date_entry = Entry(courses_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                            fg = 'black', justify = LEFT, relief = GROOVE, width = 20)      
    start_date_label.place(x = 0, y = 0 + 250)
    start_date_entry.place(x = 175, y = 0 + 250)

    '''
    Label & entry for column 'teacher_id'.
    '''       
    teacher_id_label = Label(courses_frame, text = 'Teacher - ID(FK)', font = ('Times New Roman', 15),
                                              fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    teacher_id_entry = Entry(courses_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                            fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    teacher_id_label.place(x = 0, y = 0 + 300)
    teacher_id_entry.place(x = 175, y = 0 + 300)

    '''
    Button Positioning.
    Button Y - Interval = 50.0 px
    Button X - Interval = 125.0 px
    '''
    # Button to reset all entries. command not set.
    reset_entries_button = Button(win, justify = CENTER, width = 12, bg = 'blue2', fg = 'white', text = 'Reset \n Entries',
                                          font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                          command = None)
    reset_entries_button.place(x = 400, y = 50)

    # Button to quit window.
    quit_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Quit',
                              font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                              command = win.destroy)
    quit_btn.place(x = 525, y = 50)

    return