from tkinter import *


def change_size(event):
    try:
        text.delete(1.0, END)
        width = int(e1.get())
        height = int(e2.get())
        text.config(width=width, height=height)
    except ValueError:
        text.insert(1.0, "Must enter two numbers!")

def color_lightgrey(event):
    text.config(bg='lightgrey')


def color_white(event):
    text.config(bg='white')


root = Tk()
mf = Frame()
f = Frame(mf)
e1 = Entry(f)
e1.pack()
e2 = Entry(f)
e2.pack()
f.pack(side=LEFT)
mf.pack()

b = Button(mf, text='Change')
b.pack(side=RIGHT)

text = Text(width=30, height=20)
text.pack()

b.bind('<Button-1>', change_size)
root.bind('<Return>', change_size)
text.bind('<FocusIn>', color_white)
text.bind('<FocusOut>', color_lightgrey)

root.mainloop()