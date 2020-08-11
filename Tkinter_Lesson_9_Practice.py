from tkinter import *


root = Tk()

c = Canvas(width=200, height=200, bg="white")
c.create_oval((150, 10), (190, 50), fill="orange", outline="white")
c.create_line((100, 180), (100, 60), fill="light blue", arrow=LAST, width=100, arrowshape="45 45 45")
for i in range(0, 200, 10):
    c.create_arc((i, 180), (30+i, 300+i), start=160, extent=-70, outline="green", width=3, style=ARC)
c.pack()

root.mainloop()