from tkinter import *


def to_cart():
    select = list(shop.curselection())
    select.reverse()
    for i in select:
        cart.insert(END, shop.get(i))
        shop.delete(i)


def to_shop():
    select = list(cart.curselection())
    select.reverse()
    for i in select:
        shop.insert(END, cart.get(i))
        cart.delete(i)


root = Tk()
root.title("Shop")

shop = Listbox(selectmode=EXTENDED, font=("Arial", 20))
shop.pack(side=LEFT, fill=BOTH, expand=1)

goods = ["milk", "eggs", "bananas", "tomatoes"]
for i in goods:
    shop.insert(0, i)

f = Frame()
f.pack(side=LEFT)

cart = Listbox(selectmode=EXTENDED, font=("Arial", 20))
cart.pack(side=LEFT, fill=BOTH, expand=1)

move_to_cart = Button(f, width=8, height=2, text=">>>", command=to_cart)
move_to_cart.pack()
move_to_shop = Button(f, width=8, height=2, text="<<<", command=to_shop)
move_to_shop.pack()

root.mainloop()