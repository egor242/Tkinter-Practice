from tkinter import *


def file_open():
    try:
        file_name = e.get()
        with open(file_name, encoding='UTF-8') as f:
            text.insert(1.0, f.read())
    except FileNotFoundError:
        text.delete(1.0, END)
        text.insert(1.0, "FILE DOESN'T EXIST")


def file_save():
    try:
        file_name = e.get()
        content = text.get(1.0, END)
        f = open(file_name,'w', encoding='UTF-8')
        f.write(content)
        f.close()
    except FileNotFoundError:
        text.delete(1.0, END)
        text.insert(1.0, "PLEASE ENTER THE FILE NAME")


root = Tk()
root.title('File Redactor')

frame_top = Frame()
frame_top.pack()

e = Entry(frame_top, width=20)
e.pack(side=LEFT)

b_open = Button(frame_top, text='Open', width=15, command=file_open)
b_save = Button(frame_top, text='Save', width=15, command=file_save)
b_open.pack(side=LEFT)
b_save.pack(side=LEFT)

frame_bottom = Frame()
text = Text(frame_bottom, width=50, heigh=20, wrap=NONE)
text.pack(side=LEFT, fill=BOTH, expand=1)

yscroll = Scrollbar(frame_bottom, command=text.yview, orient=VERTICAL)
yscroll.pack(side=RIGHT, fill=Y)
frame_bottom.pack(fill=BOTH, expand=1)

xscroll = Scrollbar(command=text.xview, orient=HORIZONTAL)
xscroll.pack(side=BOTTOM, fill=X)
text.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

root.mainloop()