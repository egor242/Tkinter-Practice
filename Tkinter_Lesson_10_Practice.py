from tkinter import *


def event_handler(event):
    mouse_x, mouse_y = event.x, event.y
    c.unbind("<Button-1>")

    def motion():
        x = (c.coords(ball)[0] + c.coords(ball)[2]) // 2
        y = (c.coords(ball)[1] + c.coords(ball)[3]) // 2
        dx = {
            x < mouse_x: 1,
            x == mouse_x: 0,
            x > mouse_x: -1
        }[True]
        dy = {
            y < mouse_y: 1,
            y == mouse_y: 0,
            y > mouse_y: -1
        }[True]

        c.move(ball, dx, dy)

        if (c.coords(ball)[0] + c.coords(ball)[2]) // 2 != mouse_x or (c.coords(ball)[1] + c.coords(ball)[3]) // 2 != mouse_y:
            root.after(10, motion)
        else:
            c.bind("<Button-1>", event_handler)

    motion()


root = Tk()
c = Canvas (width=400, height=400, bg='white')
ball = c.create_oval((10, 10), (50, 50), fill='green')
c.bind("<Button-1>", event_handler)
c.pack()

root.mainloop()
