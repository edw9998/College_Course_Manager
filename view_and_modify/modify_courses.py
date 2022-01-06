from tkinter import *
import tkinter.messagebox as msb

from view_and_modify.myDB import getDb, getDbError

def modify_courses_page():
    win = Tk()
    win.title("Modify Contents Of Table : 'Courses'")
    win.geometry('644x390+0+0')
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
    Functions for modifying table 'Courses'.
    '''
    def reset_entries():
        course_id_entry.delete(0, END)
        course_name_entry.delete(0, END)
        final_score_entry.delete(0, END)
        level_entry.delete(0, END)
        course_price_entry.delete(0, END)
        start_date_entry.delete(0, END)
        teacher_id_entry.delete(0, END)

    def validate_entries():
        '''
        Utility function to ensure all entries contain proper values.
        '''
        global state
        if(course_id_entry.get() == "" or course_name_entry.get() == "" or final_score_entry.get() == "" or level_entry.get() == "" or course_price_entry.get() == "" or start_date_entry.get() == "" or teacher_id_entry.get() == ""):
            state = False
        else:
            state = True
        return state
    
    def disable_foreign_keys():
        '''
        Utility function to temporarily disable foreign key constraint.
        '''
        my_db = getDb()
        my_cursor = my_db.cursor()
        my_cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS = 0")
    
    def reactivate_foreign_keys():
        '''
        Utility function to re-enable foreign key constraint.
        '''
        my_db = getDb()
        my_cursor = my_db.cursor()
        my_cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS = 1")

    def insert_to_courses():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "INSERT INTO Courses (course_id, course_name, final_score, level, course_price_usd, start_date, teacher_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            vals = (course_id_entry.get(), course_name_entry.get(), final_score_entry.get(), level_entry.get(), course_price_entry.get(), start_date_entry.get(), teacher_id_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def update_courses():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "UPDATE Courses SET course_name = %s, final_score = %s, level = %s, course_price_usd = %s, start_date = %s, teacher_id = %s WHERE course_id = %s"
            vals = (course_name_entry.get(), final_score_entry.get(), level_entry.get(), course_price_entry.get(), start_date_entry.get(), teacher_id_entry.get(), course_id_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def delete_from_courses():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "DELETE FROM Courses WHERE course_id = %s LIMIT 1"
            val = (course_id_entry.get(), )

            my_cursor.execute(query, val)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def search_in_courses():
        try:
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "SELECT course_name, final_score, level, course_price_usd, start_date, teacher_id FROM Courses WHERE course_id = %s"
            val = (course_id_entry.get(), )
            my_cursor.execute(query, val)

            # Could only fit one unique record.
            my_result = my_cursor.fetchone()

            reset_entries()
            course_id_entry.insert(0, val[0])
            course_name_entry.insert(0, my_result[0])
            final_score_entry.insert(0, my_result[1])
            level_entry.insert(0, my_result[2])
            course_price_entry.insert(0, my_result[3])
            start_date_entry.insert(0, my_result[4])
            teacher_id_entry.insert(0, my_result[5])
            msb.showinfo('Success', 'A Matching Record Was Found !')
        except getDbError() as err:
            msb.showerror('Error', str(err))

    '''
    Button Positioning.
    Button Y - Interval = 50.0 px
    Button X - Interval = 125.0 px
    '''
    # Button to reset all entries.
    reset_entries_button = Button(win, justify = CENTER, width = 12, bg = 'blue2', fg = 'white', text = 'Reset \n Entries',
                                          font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                          command = lambda: reset_entries())
    reset_entries_button.place(x = 400, y = 50)

    # Button to quit window.
    quit_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Quit',
                              font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                              command = win.destroy)
    quit_btn.place(x = 525, y = 50)

    # Button to insert data into database.
    insert_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Insert',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: insert_to_courses())
    insert_btn.place(x = 400, y = 125)

    # Button to update data in database.
    update_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Update \n By Course - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: update_courses())
    update_btn.place(x = 525, y = 125)

    # Button to delete data from database.
    delete_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Delete \n By Course - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: delete_from_courses())
    delete_btn.place(x = 400, y = 200)

    # Button to search data in database.
    search_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Search \n By Course - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: search_in_courses())
    search_btn.place(x = 525, y = 200)

    win.mainloop()
    return