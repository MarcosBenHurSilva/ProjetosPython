from tkinter import *


def do_something(event):
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y))


window = Tk()

window.bind("<Button-1>", doSomething)  # left mouse click
# window.bind("<Button-2>",doSomething) #scroll wheel
# window.bind("<Button-3>",doSomething) #right mouse click
# window.bind("<ButtonRelease>",doSomething)#mousebutton release
# window.bind("<Enter>",doSomething) #enter the windows
# window.bind("<Leave>",doSomething) #leave the windows
# window.bind("<Motion>",doSomething) #Where the mouse moved

window.mainloop()
