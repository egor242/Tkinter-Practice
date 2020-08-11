from tkinter import *


root = Tk()
first_number = Entry(root, width=20)
second_number = Entry(root, width=10)
result = Label(root, bg='black', fg='white', width=20)


def addition(event):
    try:
        one = first_number.get()
        two = second_number.get()
        res = float(one) + float(two)
    except ValueError:
        res = 'Error'
    result['text'] = res


def subtraction(event):
    try:
        one = first_number.get()
        two = second_number.get()
        res = float(one) - float(two)
    except ValueError:
        res = 'Error'
    result['text'] = res


def multiplication(event):
    try:
        one = first_number.get()
        two = second_number.get()
        res = float(one) * float(two)
    except ValueError:
        res = 'Error'
    result['text'] = res


def division(event):
    try:
        one = first_number.get()
        two = second_number.get()
        res = float(one) / float(two)
    except (ValueError, ZeroDivisionError):
        res = 'Error'
    result['text'] = res


b1 = Button(root, text='+')
b1.bind('<Button-1>', addition)
b2 = Button(root, text='-')
b2.bind('<Button-1>', subtraction)
b3 = Button(root, text='*')
b3.bind('<Button-1>', multiplication)
b4 = Button(root, text='/')
b4.bind('<Button-1>', division)

first_number.pack()
second_number.pack()
result.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()