from tkinter import *


def do_something(event):
    # print("You did a thing")
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)


window = Tk()

# window.bind("<q>", do_something)
window.bind("<Key>", do_something)
label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
