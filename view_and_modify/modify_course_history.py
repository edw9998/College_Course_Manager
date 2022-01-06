from tkinter import *
import tkinter.messagebox as msb

from view_and_modify.myDB import getDb, getDbError

def modify_course_history_page():
    win = Tk()
    win.title("Modify Contents Of Table : 'Course_History'")
    win.geometry('688x272+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'dark turquoise')

    # Title for frame.
    course_history_frame_title = Label(win, text = 'COURSE - HISTORY DETAILS', font = ("Times New Roman", 15, "bold"),
                                       bg = 'dark turquoise', fg = 'red', width = 25, justify = CENTER)
    course_history_frame_title.place(x = 40, y = 25)

    # Frame for entries.
    course_history_frame = Frame(win, bd = 5, height = 221, width = 393, bg = 'dark turquoise', relief = GROOVE)
    course_history_frame.place(x = 0, y = 50)

    '''
    Label & entry for column 'participant_id'.
    Label Y - Interval = 50.0 px Incrementation.
    Label to Entry Distance = 175.0 px. 
    '''
    participant_id_label = Label(course_history_frame, text = 'Participant - ID(PK,FK)', font = ('Times New Roman', 15),
                                           fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    participant_id_entry = Entry(course_history_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                           fg = 'black', justify = LEFT, relief = GROOVE, width = 17)
    participant_id_label.place(x = 0, y = 0)
    participant_id_entry.place(x = 205, y = 0)

    '''
    Label & entry for column 'course_id'.
    '''
    course_id_label = Label(course_history_frame, text = 'Course - ID(FK)', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    course_id_entry = Entry(course_history_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 17)
    course_id_label.place(x = 0, y = 0 + 50)
    course_id_entry.place(x = 205, y = 0 + 50)

    '''
    Functions for modifying table 'Course_History'.
    '''
    def reset_entries():
        participant_id_entry.delete(0, END)
        course_id_entry.delete(0, END)

    def validate_entries():
        '''
        Utility function to ensure all entries contain proper values.
        '''
        global state
        if(participant_id_entry.get() == '' or course_id_entry.get() == ''):
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

    def insert_to_course_history():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "INSERT INTO Course_History(participant_id, course_id) VALUES (%s, %s)"
            vals = (participant_id_entry.get(), course_id_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def update_course_history():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "UPDATE Course_History SET course_id = %s WHERE participant_id = %s"
            vals = (course_id_entry.get(), participant_id_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def delete_from_course_history():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "DELETE FROM Course_History WHERE participant_id = %s LIMIT 1" 
            val = (participant_id_entry.get())

            my_cursor.execute(query, val)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def search_in_course_history():
        try:
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "SELECT course_id FROM Course_History WHERE participant_id = %s"
            val = (participant_id_entry.get())

            # Singular value is wrapped in tuple.
            my_cursor.execute(query, (val, ))

            # Could only fit one unique record.
            my_result = my_cursor.fetchone()

            course_id_entry.delete(0, END)
            course_id_entry.insert(0, my_result[0])
            msb.showinfo('Success', 'A Matching Record Was Found !')
        except getDbError() as err:
            msb.showerror('Error', str(err))

    # Button to reset all entries.
    reset_entries_button = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Reset \n Entries',
                                          font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                          command = lambda: reset_entries())
    reset_entries_button.place(x = 400, y = 50)

    # Button to quit window.
    quit_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Quit',
                              font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                              command = win.destroy)
    quit_btn.place(x = 550, y = 50)

    # Button to insert data into database.
    insert_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Insert',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: insert_to_course_history())
    insert_btn.place(x = 400, y = 125)

    # Button to update data in database.
    update_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Update \n By Participant - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: update_course_history())
    update_btn.place(x = 550, y = 125)

    # Button to delete data from database.
    delete_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Delete \n By Participant - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: delete_from_course_history())
    delete_btn.place(x = 400, y = 200)

    # Button to search data in database.
    search_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Search \n By Participant - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: search_in_course_history())
    search_btn.place(x = 550, y = 200)

    win.mainloop()
    return