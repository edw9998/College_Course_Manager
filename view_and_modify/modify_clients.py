from tkinter import *
import tkinter.messagebox as msb

from view_and_modify.myDB import getDb, getDbError

def modify_clients_page():
    win = Tk()
    win.title("Modify Contents Of Table : 'Clients'")
    win.geometry('644x252+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'dark turquoise')

    # Title for frame.
    clients_frame_title = Label(win, text = 'CLIENT DETAILS', font = ("Times New Roman", 15, "bold"),
                                       bg = 'dark turquoise', fg = 'red', width = 20, justify = CENTER)
    clients_frame_title.place(x = 75, y = 25)

    # Frame for entries.
    clients_frame = Frame(win, bd = 5, height = 201, width = 393, bg = 'dark turquoise', relief = GROOVE)
    clients_frame.place(x = 0, y = 50)

    '''
    Label & entry for column 'client_id'.
    Label Y - Interval = 50.0 px Incrementation.
    Label to Entry Distance = 175.0 px. 
    '''
    client_id_label = Label(clients_frame, text = 'Client - ID(PK)', font = ('Times New Roman', 15),
                                           fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    client_id_entry = Entry(clients_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                           fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    client_id_label.place(x = 0, y = 0)
    client_id_entry.place(x = 175, y = 0)

    '''
    Label & entry for column 'client_name'.
    '''
    client_name_label = Label(clients_frame, text = 'Client Name', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    client_name_entry = Entry(clients_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    client_name_label.place(x = 0, y = 0 + 50)
    client_name_entry.place(x = 175, y = 0 + 50)

    '''
    Label & entry for column 'address'.
    '''
    address_label = Label(clients_frame, text = 'Address', font = ('Times New Roman', 15),
                                             fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    address_entry = Entry(clients_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                             fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    address_label.place(x = 0, y = 0 + 100)
    address_entry.place(x = 175, y = 0 + 100)

    '''
    Label & entry for column 'industry'.
    '''
    industry_label = Label(clients_frame, text = 'Industry', font = ('Times New Roman', 15),
                                         fg = 'tomato', bg = 'dark turquoise', justify = LEFT)
    industry_entry = Entry(clients_frame, bg = 'cyan', bd = 3, font = ('Times New Roman', 15, 'bold'),
                                       fg = 'black', justify = LEFT, relief = GROOVE, width = 20)
    industry_label.place(x = 0, y = 0 + 150)
    industry_entry.place(x = 175, y = 0 + 150)

    '''
    Functions for modifying table 'Clients'.
    '''
    def reset_entries():
        client_id_entry.delete(0, END)
        client_name_entry.delete(0, END)
        address_entry.delete(0, END)
        industry_entry.delete(0, END)

    def validate_entries():
        '''
        Utility function to ensure all entries contain proper values.
        '''
        global state
        if(client_id_entry.get() == '' or client_name_entry.get() == '' or address_entry.get() == '' or industry_entry.get() == ''):
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

    def insert_to_clients():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "INSERT INTO Clients(client_id, client_name, address, industry) VALUES (%s, %s, %s, %s)"
            vals = (client_id_entry.get(), client_name_entry.get(), address_entry.get(), industry_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def update_clients():
        if(validate_entries() == False):
            msb.showwarning('Warning', 'Please Fill In All Textfields Properly.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "UPDATE Clients SET client_name = %s, address = %s, industry = %s WHERE client_id = %s"
            vals = (client_name_entry.get(), address_entry.get(), industry_entry.get(), client_id_entry.get())

            my_cursor.execute(query, vals)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def delete_from_clients():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "DELETE FROM Clients WHERE client_id = %s LIMIT 1"
            val = (client_id_entry.get(), )

            my_cursor.execute(query, val)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def search_in_clients():
        try:
            my_db = getDb()
            my_cursor = my_db.cursor()

            query = "SELECT client_name, address, industry FROM Clients WHERE client_id = %s"
            val = (client_id_entry.get(), )
            my_cursor.execute(query, val)

            # Could only fit one unique record.
            my_result = my_cursor.fetchone()

            reset_entries()
            client_id_entry.insert(0, val[0])
            client_name_entry.insert(0, my_result[0])
            address_entry.insert(0, my_result[1])
            industry_entry.insert(0, my_result[2])
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
                                command = lambda: insert_to_clients())
    insert_btn.place(x = 400, y = 125)

    # Button to update data in database.
    update_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Update \n By Client - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: update_clients())
    update_btn.place(x = 525, y = 125)

    # Button to delete data from database.
    delete_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Delete \n By Client - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: delete_from_clients())
    delete_btn.place(x = 400, y = 200)

    # Button to search data in database.
    search_btn = Button(win, justify = CENTER, width = 12, height = 2, bg = 'blue2', fg = 'white', text = 'Search \n By Client - ID',
                                font = ('Times New Roman', 12, "bold"), activebackground = None, relief = GROOVE,
                                command = lambda: search_in_clients())
    search_btn.place(x = 525, y = 200)

    win.mainloop()
    return