from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from tkinter.ttk import Scrollbar

from view_and_modify.myDB import getDb, getDbError

def view_courses_page():
    win = Tk()
    win.title("View Table : 'Courses'")
    win.geometry("1142x600")                            # (width x height)
    win.resizable(height = False, width = False)
    win.config(bg = "dark sea green")

    # Retrieve all rows and keep them in cursor.
    myDb = getDb()
    myCursor = myDb.cursor()
    myCursor.execute("SELECT * FROM Courses")

    tree = Treeview(win, selectmode = 'browse', height = 25)

    # Omit the first empty column.
    tree["show"] = "headings"

    # Style the treeview columns and rows.
    style = Style(win)
    style.theme_use("clam")                                                                             # Table style.
    style.configure("Treeview.Heading", font = ("Times New Roman", 12, "bold"), foreground = "blue")    # Heading(columns)
    style.configure(".", font = ("Times New Roman", 12))                                                # Rows

    # Define the columns.
    tree["columns"] = ("course_id", "course_name", "final_score", "level", "course_price_usd", "start_date", "teacher_id")

    # Assign column width, min-width attributes & align column names to center.
    tree.column("course_id", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("course_name", width = 225, minwidth = 225, anchor = CENTER)
    tree.column("final_score", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("level", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("course_price_usd", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("start_date", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("teacher_id", width = 150, minwidth = 150, anchor = CENTER)

    # Assign column heading names.
    tree.heading("course_id", text = "Course-ID", anchor = CENTER)
    tree.heading("course_name", text = "Course Name", anchor = CENTER)
    tree.heading("final_score", text = "Final Score", anchor = CENTER)
    tree.heading("level", text = "Level", anchor = CENTER)
    tree.heading("course_price_usd", text = "Course Price(US$)", anchor = CENTER)
    tree.heading("start_date", text = "Start Date", anchor = CENTER)
    tree.heading("teacher_id", text = "Teacher-ID", anchor = CENTER)

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
    table_size_label = Label(win, text = "Current Shape Of Table =", font = ("Times New Roman", 15, "bold"), 
                                    bg = "dark sea green", fg = "aquamarine", width = 20, justify = CENTER)
    table_size_label.place(x = -10, y = 550)

    # Read-onlyentry to display shape and size of table.
    table_size_entry = Entry(win, width = 31, bg = "dark sea green", fg = "red", font = ("Times New Roman", 20, "bold"), 
                                justify = LEFT)
    table_size_entry.insert(0, '('+ str(start) + 'x' + str(len(row))+')' + " <<>> (N_Rows x N_Columns)")
    table_size_entry.configure(state = "readonly")
    table_size_entry.place(x = 230, y = 547)

    # Display this sub-window.
    win.mainloop()
    return