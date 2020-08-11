from tkinter import *


def show_info():
    if var1.get() in friends_db.keys():
        label['text'] = friends_db[var1.get()]


friends_db = {"Oleg": "8-921-**", "Emil": "8-916-**", "Pavel": "8-922-**", "Egor": "8-931-**", "Denis": "8-977-**"}

root = Tk()
root.title('Phone Book')
button_frame = Frame()
label = Label(width=35, height=15)
var1 = StringVar()

for name in friends_db.keys():
    Radiobutton(button_frame, width=15, height=5, variable=var1, value=name, indicatoron=0, text=name,
                command=show_info).pack(fill=BOTH, expand=1)

button_frame.pack(side=LEFT)
label.pack(fill=BOTH, expand=1)

root.mainloop()