# radio button = similar to checkbox, but you can only select one from a group.

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh!")

window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
hamburgerImage = PhotoImage(file='hamburger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],  # add text to radio buttons
                               variable=x,  # group radiobutton together if they share the same variable
                               value=index,  # assigns each radiobutton a different value
                               padx=25,
                               font=("Impact", 50),
                               image=foodImages[index],  # adds image to radio button
                               compound='left',  # adds image and text (left-side)
                               indicatoron=0,  # eliminate circle indicator
                               width=800,  # sets width of radiobuttons
                               command=order  # set command to radiobutton to function
                               )
    radio_button.pack(anchor=W)

window.mainloop()
