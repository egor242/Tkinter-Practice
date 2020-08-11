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
mainmenu = Menu()
root.config(menu=mainmenu)
mainmenu.add_command(label="Open", command=insert_text)
mainmenu.add_command(label="Save", command=extract_text)

text = Text(width=50, height=20)
text.pack()

context_menu = Menu(tearoff=0)
context_menu.add_command(label="Clear", command=clear)
text.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

root.mainloop()