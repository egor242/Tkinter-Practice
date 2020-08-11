from tkinter import *


def add_figure():
    figure_window = Toplevel()
    figure_window.title("Draw figure")
    figure_window.update_idletasks()
    figure_window.geometry('200x200+600+100')
    figure_window.resizable(False, False)

    Label(figure_window, text="x1").grid(row=0, column=0, sticky=E)
    e_x1 = Entry(figure_window, width=4)
    e_x1.grid(row=0, column=1, sticky=W, padx=10)
    Label(figure_window, text="y1").grid(row=0, column=2, padx=5)
    e_y1 = Entry(figure_window, width=4)
    e_y1.grid(row=0, column=3, sticky=W)

    Label(figure_window, text="x2").grid(row=1, column=0, sticky=E)
    e_x2 = Entry(figure_window, width=4)
    e_x2.grid(row=1, column=1, sticky=W, padx=10)
    Label(figure_window, text="y2").grid(row=1, column=2, padx=5)
    e_y2 = Entry(figure_window, width=4)
    e_y2.grid(row=1, column=3, sticky=W)

    r_var = BooleanVar()
    r_var.set(0)
    rect_button = Radiobutton(figure_window, text="Rectangle", variable=r_var, value=0)
    oval_button = Radiobutton(figure_window, text="Oval", variable=r_var, value=1)
    rect_button.grid(row=2, column=0, columnspan=4, padx=10, sticky=W+E, pady=5)
    oval_button.grid(row=3, column=0, columnspan=4, padx=10, sticky=W+E)

    Label(figure_window, text="Fill").grid(row=4, column=0, padx=10, pady=5)
    e_fill = Entry(figure_window, width=15)
    e_fill.insert(0, "white")
    e_fill.grid(row=4, column=1, columnspan=3)

    Label(figure_window, text="Outline").grid(row=5, column=0, padx=10)
    e_outline = Entry(figure_window, width=15)
    e_outline.insert(0, "black")
    e_outline.grid(row=5, column=1, columnspan=3)

    def draw_figure():
        if r_var.get() == 0:
            c.create_rectangle(e_x1.get(), e_y1.get(), e_x2.get(), e_y2.get(), fill=e_fill.get(),
                               outline=e_outline.get(), width=3)
            figure_window.destroy()
        else:
            c.create_oval(e_x1.get(), e_y1.get(), e_x2.get(), e_y2.get(), fill=e_fill.get(),
                          outline=e_outline.get(), width=3)
            figure_window.destroy()

    draw_button = Button(figure_window, text='Draw', command=draw_figure)
    draw_button.grid(row=6, column=0, columnspan=4, pady=10)


root = Tk()
root.update_idletasks()
root.geometry('+30+30')
c = Canvas(root, width=500, height=500, bg='white')
c.pack(fill=BOTH)
add_button = Button(root, text="Add figure", command=add_figure)
add_button.pack()

root.mainloop()
