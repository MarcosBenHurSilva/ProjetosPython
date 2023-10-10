# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.pack(side=TOP  )

Button(frame, text="W", font=("CONSOLAS", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("CONSOLAS", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("CONSOLAS", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("CONSOLAS", 25), width=3).pack(side=LEFT)

window.mainloop()
