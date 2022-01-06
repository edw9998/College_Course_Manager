from tkinter import *
import tkinter.messagebox as msb

from view_and_modify.myDB import getDb, getDbError

def modify_participants_page():
    win = Tk()
    win.title("Modify Contents Of Table : 'Participants'")
    win.geometry('727x392+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'dark turquoise')

    # Title for frame.
    participants_frame_title = Label(win, text = 'PARTICIPANT DETAILS', font = ('Times New Roman', 15, "bold"), 
                                        fg = 'red', bg = 'dark turquoise', width = 20, justify = CENTER)
    participants_frame_title.place(x = 80, y = 25)

    # Frame as container for entries.
    participants_frame = Frame(win, bd = 5, height = 341, width = 428, bg = 'dark turquoise', relief = GROOVE)
    participants_frame.place(x = 0, y = 50)

    '''
    Label & entry for column 'participant_id'.
    Label Y - Interval = 50.0 px Incrementation.
    Label to Entry Distance = 150.0 px. 
    '''
    participant_id_label = Label(participants_frame, text = 'Participant - ID(PK)', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    participant_id_entry = Entry(participants_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 24)
    participant_id_label.place(x = 0, y = 0)
    participant_id_entry.place(x = 170, y = 0)

    '''
    Label & entry for column 'first_name'.
    '''
    first_name_label = Label(participants_frame, text = 'First Name', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    first_name_entry = Entry(participants_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 24)
    first_name_label.place(x = 0, y = 0 + 50)
    first_name_entry.place(x = 170, y = 0 + 50)

    '''
    Label & entry for column 'last_name'.
    '''
    last_name_label = Label(participants_frame, text = 'Last Name', font = ('Times New Roman', 15),
                                            fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    last_name_entry = Entry(participants_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                            fg = 'black', justify = LEFT, relief = GROOVE, width = 24)
    last_name_label.place(x = 0, y = 0 + (50 * 2))
    last_name_entry.place(x = 170, y = 0 + (50 * 2))

    '''
    Label & entry for column 'phone_no'.
    '''
    phone_no_label = Label(participants_frame, text = 'Phone Number', font = ('Times New Roman', 15),
                                                    fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    phone_no_entry = Entry(participants_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                                    fg = 'black', justify = LEFT, relief = GROOVE, width = 24)
    phone_no_label.place(x = 0, y = 0 + (50 * 3))
    phone_no_entry.place(x = 170, y = 0 + (50 * 3))

    '''
    Label & entry for column 'client_designated'.
    '''
    client_designated_label = Label(participants_frame, text = 'Client Designated', font = ('Times New Roman', 15),
                                                 fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    client_designated_entry = Entry(participants_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, "bold"),
                                                 fg = 'black', justify = LEFT, relief = GROOVE, width = 24)
    client_designated_label.place(x = 0, y = 0 + (50 * 4))
    client_designated_entry.place(x = 170, y = 0 + (50 * 4))

    '''
    Functions for modifying table 'Participants'.
    '''
    def reset_entries():
        participant_id_entry.delete(0, END)
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        phone_no_entry.delete(0, END)
        client_designated_entry.delete(0, END)

    def validate_entries():
        '''
        Utility function to ensure all entries contain proper values.
        '''
        global state
        if(participant_id_entry.get() == '' or first_name_entry.get() == '' or last_name_entry.get() == '' or phone_no_entry.get() == '' or client_designated_entry.get() == ''):
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

    def insert_to_participants():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "INSERT INTO Participants (participant_id, first_name, last_name, phone_no, client_designated) VALUES (%s, %s, %s, %s, %s)"
            vals = (participant_id_entry.get(), first_name_entry.get(), last_name_entry.get(), phone_no_entry.get(), client_designated_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def update_participants():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "UPDATE Participants SET first_name = %s, last_name = %s, phone_no = %s, client_designated = %s WHERE participant_id = %s"
            vals = (first_name_entry.get(), last_name_entry.get(), phone_no_entry.get(), client_designated_entry.get(), participant_id_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def delete_from_participants():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "DELETE FROM Participants WHERE participant_id = %s LIMIT 1"
            val = (participant_id_entry.get(), )

            my_cursor.execute(query, val)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def search_in_participants():
        try:
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "SELECT first_name, last_name, phone_no, client_designated FROM Participants WHERE participant_id = %s"
            val = (participant_id_entry.get(), )
            my_cursor.execute(query, val)

            # Could only fit one unique record.
            my_result = my_cursor.fetchone()

            reset_entries()
            participant_id_entry.insert(0, val[0])
            first_name_entry.insert(0, my_result[0])
            last_name_entry.insert(0, my_result[1])
            phone_no_entry.insert(0, my_result[2])
            client_designated_entry.insert(0, my_result[3])
            msb.showinfo('Success', 'A Matching Record Was Found !')
        except getDbError() as err:
            msb.showerror('Error', str(err))

    '''
    Button Positioning.
    Button X - Interval = 150.0 px
    Button Y - Interval = 100.0 px
    '''
    # Button to reset all entries.
    reset_entries_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Reset \n Entries',
                                    font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                    command = lambda: reset_entries())
    reset_entries_btn.place(x = 440, y = 119)

    # Button to quit window.
    quit_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Quit',
                           font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                           command = win.destroy)
    quit_btn.place(x = 440 + 150, y = 119)

    # Button to insert data into table.
    insert_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Insert',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: insert_to_participants())
    insert_btn.place(x = 440, y = 119 + 100)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Update \n By Participant - ID',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: update_participants())
    update_btn.place(x = 440 + 150, y = 119 + 100)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Delete \n By Participant - ID',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: delete_from_participants())
    delete_btn.place(x = 440, y = 119 + (100 * 2))

    # Button to search data from table referencing PK.
    search_btn = Button(win, justify = CENTER, width = 14, height = 3, bg = 'blue2', fg = 'white', text = 'Search \n By Participant - ID',
                             font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                             command = lambda: search_in_participants())
    search_btn.place(x = 440 + 150, y = 119 + (100 * 2))

    win.mainloop()
    return