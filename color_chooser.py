from tkinter import *
from tkinter import colorchooser  # submodule


def click():
    color = colorchooser.askcolor()  # assign color to a variable
    print(color)
    colorHex = color[1]  # assigns element at index 1 to a variable
    window.config(bg=colorHex)  # change background color
    # window.config(bg=colorchooser.askcolor()[1])  # função toda em uma linha


window = Tk()
window.geometry("420x420")
button = Button(text='click me', command=click)
button.pack()
window.mainloop()
