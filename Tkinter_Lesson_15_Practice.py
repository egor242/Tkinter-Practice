from tkinter import *
from random import uniform


def random_pos(event):
    #a, = root.winfo_children()
    #a.destroy()
    #new_but = Button(image=img)
    #new_but.place(relx=uniform(0.1, 0.85), rely=uniform(0.1, 0.85), relwidth=0.2, relheight=0.2)
    #new_but.bind('<Button-1>', random_pos)
    but.place(relx=uniform(0.1, 0.85), rely=uniform(0.1, 0.85))


root = Tk()
root.geometry('500x500')
img = PhotoImage(file='smile.gif')
but = Button(image=img)
but.place(relx=uniform(0.1, 0.85), rely=uniform(0.1, 0.85), width=80, height=80)
but.bind('<Button-1>', random_pos)

root.mainloop()