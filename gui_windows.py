from tkinter import *

window = Tk()  # instantiate an insurance of a window
window.geometry("720x480")
window.title("Marcos first GUI program")

icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background="black")

window.mainloop()  # place window on computer screen, listen for events
