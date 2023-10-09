from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees Cº")


window = Tk()

hotImage = PhotoImage(file='hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # VERTICAL OR HORIZONTAL
              font=('Consolas', 20),  # adds numeric indicators for value
              tickinterval=10,  # hide current value
              # showvalue=0,
              resolution=5,  # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])  # set current value of  slider
scale.pack()

snowImage = PhotoImage(file='snow.png')
snowLabel = Label(image=snowImage)
snowLabel.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
