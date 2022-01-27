from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from tkinter.ttk import Scrollbar

from view_and_modify.myDB import getDb, getDbError

def view_teachers_page():
    win = Tk()
    win.title("View Table : 'Teachers'")
    win.geometry("1067x600")                            # (width x height)
    win.resizable(height = False, width = False)
    win.config(bg = "dark sea green")

    # Retrieve all rows and keep them in cursor.
    myDb = getDb()
    myCursor = myDb.cursor()
    myCursor.execute("SELECT * FROM Teachers")

    tree = Treeview(win, selectmode = 'browse', height = 25)

    # Omit the first empty column.
    tree["show"] = "headings"

    # Style the treeview columns and rows.
    style = Style(win)
    style.theme_use("clam")                                                                             # Table style.
    style.configure("Treeview.Heading", font = ("Times New Roman", 12, "bold"), foreground = "blue")    # Heading(columns)
    style.configure(".", font = ("Times New Roman", 12))                                                # Rows

    # Define the columns.
    tree["columns"] = ("teacher_id", "first_name", "last_name", "language_utilized", "teachingSince", "tax_id", "phone_number")

    # Assign column width, min-width attributes & align column names to center.
    tree.column("teacher_id", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("first_name", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("last_name", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("language_utilized", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("teachingSince", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("tax_id", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("phone_number", width = 150, minwidth = 150, anchor = CENTER)

    # Assign column heading names.
    tree.heading("teacher_id", text = "Teacher-ID", anchor = CENTER)
    tree.heading("first_name", text = "First Name", anchor = CENTER)
    tree.heading("last_name", text = "Last Name", anchor = CENTER)
    tree.heading("language_utilized", text = "Language Utilized", anchor = CENTER)
    tree.heading("teachingSince", text = "Teaching Since", anchor = CENTER)
    tree.heading("tax_id", text = "Tax-ID", anchor = CENTER)
    tree.heading("phone_number", text = "Phone Number", anchor = CENTER)

    # Iterate through and insert rows from the 'teacher' table in database into treeview.
    # start variable tells how many rows available in treeview.
    start = 0
    for row in myCursor:
        tree.insert("", start, text = "", values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        start = start + 1
    
    # Vertical scrollbar for treeview.
    vsb = Scrollbar(win, orient = "vertical")
    vsb.configure(command = tree.yview)

    # Add the vertical scrollbar to the right of treeview.
    tree.configure(yscrollcommand = vsb.set)
    vsb.pack(fill = Y, side = RIGHT)

    # Display treeview(table) at center & top positions.
    tree.place(x = 0, y = 0)

    # Label for entry to display shape and size of table.
    table_size_label = Label(win, text = "Number Of Records =", font = ("Times New Roman", 15, "bold"), 
                                    bg = "dark sea green", fg = "aquamarine", width = 20, justify = CENTER)
    table_size_label.place(x = -10, y = 550)

    # Read-onlyentry to display shape and size of table.
    table_size_entry = Entry(win, width = 31, bg = "dark sea green", fg = "red", font = ("Times New Roman", 20, "bold"), 
                                justify = LEFT)
    table_size_entry.insert(0, str(start))
    table_size_entry.configure(state = "readonly")
    table_size_entry.place(x = 230, y = 547)

    # Display this sub-window.
    win.mainloop()
    return