from tkinter import *
from PIL import ImageTk, Image

def view_database_er_page():
    win = Tk()
    win.geometry("700x500")
    win.resizable(height = True, width = True)

    frame = Frame(win, width = 600, height = 400)
    frame.pack()
    frame.place(anchor = 'center', relx = 0.5, rely = 0.5)

    img = ImageTk.PhotoImage(master = win, image = Image.open("images\my_er.jpg"))

    label = Label(frame, image = img)
    label.pack()

    win.mainloop()
    return