from tkinter import *


def to_list(event):
    text = e.get()
    e.delete(0, END)
    lb.insert(END, text)


def to_entry(event):
    e.delete(0, END)
    select = lb.curselection()
    e.insert(0, lb.get(select))


root = Tk()
e = Entry(width=30)
e.bind('<Return>', to_list)
e.pack()
lb = Listbox(width=30, height=15)
lb.bind('<Double-Button-1>', to_entry)
lb.pack()

root.mainloop()