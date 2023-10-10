from tkinter import *


def do_something(event):
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y))


window = Tk()

window.bind("<Button-1>", do_something)  # left mouse click
# window.bind("<Button-2>",do_something)  # scroll wheel
# window.bind("<Button-3>",do_something)  # right mouse click
# window.bind("<ButtonRelease>",do_something)  # mouse button release
# window.bind("<Enter>",do_something)  # enter the windows
# window.bind("<Leave>",do_something)  # leave the windows
# window.bind("<Motion>",do_something)  # Where the mouse moved

window.mainloop()
