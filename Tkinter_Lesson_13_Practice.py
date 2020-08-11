from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def insert_text():
    file_name = fd.askopenfilename()
    if file_name:
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    else:
        mb.showerror("Error", "File is not chosen")


def extract_text():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("Python files", "*.py"),
                                                ("All files", "*.*")))
    if file_name:
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    else:
        mb.showerror("Error", "File to save the text is not chosen")


def clear():
    answer = mb.askyesno("Warning", "Are you sure you want to delete the text?")
    if answer:
        text.delete(1.0, END)


root = Tk()

text = Text(width=50, height=20)
text.grid(columnspan=3)
b1 = Button(text="Open", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Save", command=extract_text)
b2.grid(row=1, column=1)
b3 = Button(text="Clear", command=clear)
b3.grid(row=1, column=2, sticky=W)

root.mainloop()