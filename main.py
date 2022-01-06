# Main page for the app.
from tkinter import *

from view_and_modify.view_database_er import view_database_er_page
from view_and_modify.view_teachers import view_teachers_page
from view_and_modify.view_courses import view_courses_page
from view_and_modify.view_clients import view_clients_page
from view_and_modify.view_participants import view_participants_page
from view_and_modify.view_course_history import view_course_history_page

from view_and_modify.modify_teachers import modify_teachers_page
from view_and_modify.modify_courses import modify_courses_page
from view_and_modify.modify_clients import modify_clients_page
from view_and_modify.modify_participants import modify_participants_page
from view_and_modify.modify_course_history import modify_course_history_page

# Main window.
root = Tk()                                             # Create main window.
root.geometry("750x600+0+0")                            # (width x height) + (shift_x) + (shift_y)
root.resizable(height = False, width = False)           # Disable resizing.
root.title("Online Course Database Management System")  
root.iconbitmap("images\icon.jpg")                      # Set icon.
root.config(bg = "dark goldenrod")              

# Create menu bar to view tables.
Menu_Bar = Menu(root)
Table_Menu = Menu(Menu_Bar, tearoff = 0)
Table_Menu.add_command(label = 'View E-R Diagram', command = lambda: view_database_er_page())
Table_Menu.add_separator()
Table_Menu.add_command(label = 'View Table \'Teachers\'', command = lambda: view_teachers_page())
Table_Menu.add_separator()
Table_Menu.add_command(label = 'View Table \'Courses\'', command = lambda: view_courses_page())
Table_Menu.add_separator()
Table_Menu.add_command(label = 'View Table \'Clients\'', command = lambda: view_clients_page())
Table_Menu.add_separator()
Table_Menu.add_command(label = 'View Table \'Participants\'', command = lambda: view_participants_page())
Table_Menu.add_separator()
Table_Menu.add_command(label = 'View Table \'Course_History\'', command = lambda: view_course_history_page())
Table_Menu.add_separator()
Menu_Bar.add_cascade(label = 'More Info', menu = Table_Menu)

Exit_Menu = Menu(Menu_Bar, tearoff = 0)
Exit_Menu.add_command(label = 'Quit Here', command = root.destroy)
Exit_Menu.add_separator()
Menu_Bar.add_cascade(label = 'Quit', menu = Exit_Menu)

# Label / title.
title = Label(root, text = 'Course Database Management', font = ("Times New Roman", 35, "bold"), 
                    bg = 'gray', fg = 'gray10', width = 40, justify = CENTER)
title.place(x = -187, y = 0)

'''
Button Y - Interval = 110.0
'''
# Button to access table 'Teachers'.
teachers_btn = Button(root, justify = CENTER, width = 27, bg = "gold", fg = "RoyalBlue4", text = "1) Modify Table \'Teachers\'", 
                            font = ("Times New Roman", 25, "bold"), activebackground = None, relief = GROOVE, 
                            command = lambda: modify_teachers_page())
teachers_btn.place(x = 98, y = 75)

# Button to access table 'Courses'.
courses_btn = Button(root, justify = CENTER, width = 27, bg = "gold", fg = "RoyalBlue4", text = "2) Modify Table \'Courses\'", 
                           font = ("Times New Roman", 25, "bold"), activebackground = None, relief = GROOVE, 
                           command = lambda: modify_courses_page())
courses_btn.place(x = 98, y = 75 + (1 * 110.0))

# Button to access table 'Clients'.
clients_btn = Button(root, justify = CENTER, width = 27, bg = "gold", fg = "RoyalBlue4", text = "3) Modify Table \'Clients\'", 
                           font = ("Times New Roman", 25, "bold"), activebackground = None, relief = GROOVE, 
                           command = lambda: modify_clients_page())
clients_btn.place(x = 98, y = 75 + (2 * 110.0))

# Button to access table 'Participants'.
participants_btn = Button(root, justify = CENTER, width = 27, bg = "gold", fg = "RoyalBlue4", text = "4) Modify Table \'Participants\'", 
                                font = ("Times New Roman", 25, "bold"), activebackground = None, relief = GROOVE, 
                                command = lambda: modify_participants_page())
participants_btn.place(x = 98, y = 75 + (3 * 110.0))

# Button to access table 'Course_History'. 
course_history_btn = Button(root, justify = CENTER, width = 27, bg = "gold", fg = "RoyalBlue4", text = "5) Modify Table \'Course_History\'", 
                                  font = ("Times New Roman", 25, "bold"), activebackground = None, relief = GROOVE, 
                                  command = lambda: modify_course_history_page())
course_history_btn.place(x = 98, y = 75 + (4 * 110.0))

# Run app.
if __name__ == '__main__':
    root.config(menu = Menu_Bar)
    root.mainloop()