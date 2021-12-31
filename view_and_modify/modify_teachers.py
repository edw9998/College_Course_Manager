from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView

from view_and_modify.myDB import getDb, getDbError

def modify_teachers_page():
    win = Tk()
    win.title("Modify Contents Of Table : 'Teachers'")
    win.geometry('709x392+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'dark turquoise')

    # Title for frame.
    teachers_frame_title = Label(win, text = 'TEACHER DETAILS', font = ('Times New Roman', 15, "bold"), 
                                        fg = 'red', bg = 'dark turquoise', width = 20, justify = CENTER)
    teachers_frame_title.place(x = 80, y = 25)

    # Frame as container for entries.
    teachers_frame = Frame(win, bd = 5, height = 341, width = 419, bg = 'dark turquoise', relief = GROOVE)
    teachers_frame.place(x = 0, y = 50)

    '''
    Label & entry for column 'teacher_id'.
    Label Y - Interval = 50.0 px Incrementation.
    Label to Entry Distance = 150.0 px. 
    '''
    teacher_id_label = Label(teachers_frame, text = 'Teacher - ID(PK)', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    teacher_id_entry = Entry(teachers_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 25)
    teacher_id_label.place(x = 0, y = 0)
    teacher_id_entry.place(x = 150, y = 0)

    '''
    Label & entry for column 'first_name'.
    '''
    first_name_label = Label(teachers_frame, text = 'First Name', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    first_name_entry = Entry(teachers_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 25)
    first_name_label.place(x = 0, y = 0 + 50)
    first_name_entry.place(x = 150, y = 0 + 50)

    '''
    Label & entry for column 'last_name'.
    '''
    last_name_label = Label(teachers_frame, text = 'Last Name', font = ('Times New Roman', 15),
                                            fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    last_name_entry = Entry(teachers_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                            fg = 'black', justify = LEFT, relief = GROOVE, width = 25)
    last_name_label.place(x = 0, y = 0 + (50 * 2))
    last_name_entry.place(x = 150, y = 0 + (50 * 2))

    '''
    Label & entry for column 'language_utilized'.
    '''
    language_utilized_label = Label(teachers_frame, text = 'Language Utilized', font = ('Times New Roman', 15),
                                                    fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    language_utilized_entry = Entry(teachers_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                                    fg = 'black', justify = LEFT, relief = GROOVE, width = 25)
    language_utilized_label.place(x = 0, y = 0 + (50 * 3))
    language_utilized_entry.place(x = 150, y = 0 + (50 * 3))

    '''
    Label & entry for column 'teaching_since'.
    '''
    teaching_since_label = Label(teachers_frame, text = 'Teaching Since', font = ('Times New Roman', 15),
                                                 fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    teaching_since_entry = Entry(teachers_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                                 fg = 'black', justify = LEFT, relief = GROOVE, width = 25)
    teaching_since_label.place(x = 0, y = 0 + (50 * 4))
    teaching_since_entry.place(x = 150, y = 0 + (50 * 4))

    '''
    Label & entry for column 'tax_id'.
    '''
    tax_id_label = Label(teachers_frame, text = 'Tax - ID(AK)', font = ('Times New Roman', 15),
                                         fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    tax_id_entry = Entry(teachers_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                         fg = 'black', justify = LEFT, relief = GROOVE, width = 25)
    tax_id_label.place(x = 0, y = 0 + (50 * 5))
    tax_id_entry.place(x = 150, y = 0 + (50 * 5))

    '''
    Label & entry for column 'phone_number'.
    '''
    phone_number_label = Label(teachers_frame, text = 'Phone Number', font = ('Times New Roman', 15),
                                               fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    phone_number_entry = Entry(teachers_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                               fg = 'black', justify = LEFT, relief = GROOVE, width = 25)
    phone_number_label.place(x = 0, y = 0 + (50 * 6))
    phone_number_entry.place(x = 150, y = 0 + (50 * 6))

    '''
    Functions for modifying table 'Teachers'.
    '''
    def reset_entries():
        teacher_id_entry.delete(0, END)
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        language_utilized_entry.delete(0, END)
        teaching_since_entry.delete(0, END)
        tax_id_entry.delete(0, END)
        phone_number_entry.delete(0, END)

    def validate_entries():
        '''
        Utility function to ensure all entries contain proper values.
        '''
        global state
        if(teacher_id_entry.get() == "" or first_name_entry.get() == "" or last_name_entry.get() == "" or language_utilized_entry.get() == "" or teaching_since_entry.get() == "" or tax_id_entry.get() == "" or phone_number_entry.get() == ""):
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

    def insert_to_teachers():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "INSERT INTO Teachers(teacher_id, first_name, last_name, language_utilized, teachingSince, tax_id, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            vals = (teacher_id_entry.get(), first_name_entry.get(), last_name_entry.get(), language_utilized_entry.get(), teaching_since_entry.get(), tax_id_entry.get(), phone_number_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def update_teachers():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "UPDATE Teachers SET first_name = %s, last_name = %s, language_utilized = %s, teachingSince = %s, tax_id = %s, phone_number = %s WHERE teacher_id = %s"
            vals = (first_name_entry.get(), last_name_entry.get(), language_utilized_entry.get(), teaching_since_entry.get(), tax_id_entry.get(), phone_number_entry.get(), teacher_id_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def delete_from_teachers():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "DELETE FROM Teachers WHERE teacher_id = %s LIMIT 1"
            val = (teacher_id_entry.get(), )

            my_cursor.execute(query, val)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def search_in_teachers():
        try:
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "SELECT first_name, last_name, language_utilized, teachingSince, tax_id, phone_number FROM Teachers WHERE teacher_id = %s"
            val = (teacher_id_entry.get(), )
            my_cursor.execute(query, val)

            # Could only fit one unique record.
            my_result = my_cursor.fetchone()

            reset_entries()
            teacher_id_entry.insert(0, val[0])
            first_name_entry.insert(0, my_result[0])
            last_name_entry.insert(0, my_result[1])
            language_utilized_entry.insert(0, my_result[2])
            teaching_since_entry.insert(0, my_result[3])
            tax_id_entry.insert(0, my_result[4])
            phone_number_entry.insert(0, my_result[5])
            msb.showinfo('Success', 'A Matching Record Was Found !')
        except getDbError() as err:
            msb.showerror('Error', str(err))

    '''
    Button Positioning.
    Button X - Interval = 150.0 px
    Button Y - Interval = 100.0 px
    '''
    # Button to reset all entries.
    reset_entries_btn = Button(win, justify = CENTER, width = 12, bg = 'blue2', fg = 'white', text = 'Reset \n Entries',
                                    font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                    command = lambda: reset_entries())
    reset_entries_btn.place(x = 440, y = 119)

    # Button to quit window.
    quit_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Quit',
                           font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                           command = win.destroy)
    quit_btn.place(x = 440 + 150, y = 119)

    # Button to insert data into table.
    insert_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Insert',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: insert_to_teachers())
    insert_btn.place(x = 440, y = 119 + 100)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 12, bg = 'blue2', fg = 'white', text = 'Update \n By Teacher - ID',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: update_teachers())
    update_btn.place(x = 440 + 150, y = 119 + 100)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 12, bg = 'blue2', fg = 'white', text = 'Delete \n By Teacher - ID',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: delete_from_teachers())
    delete_btn.place(x = 440, y = 119 + (100 * 2))

    # Button to search data from table referencing PK.
    search_btn = Button(win, justify = CENTER, width = 12, bg = 'blue2', fg = 'white', text = 'Search \n By Teacher - ID',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: search_in_teachers())
    search_btn.place(x = 440 + 150, y = 119 + (100 * 2))

    win.mainloop()
    return