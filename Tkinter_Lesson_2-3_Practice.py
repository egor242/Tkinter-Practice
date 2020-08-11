from tkinter import *
from functools import partial


root = Tk()
l = Label(width=20)
e = Entry(width=24, justify=CENTER)
f_bot = Frame(root)
l.pack(pady=10)
e.pack(pady=10)
f_bot.pack()
colors = {"Red": "#ff0000", "Orange": "#ff7d00", "Yellow": "#ffff00", "Green": "#00ff00",
          "Light blue": "#007dff", "Blue": "#0000ff", "Purple": "#7d00ff"}


def change_color(n):
    l['text'] = n
    e.delete(0, END)
    e.insert(0, colors[n])


for key in colors.keys():
    Button(f_bot, bg=key, width=5, height=2, command=partial(change_color, key)).pack(side=LEFT, padx=2)

root.mainloop()
