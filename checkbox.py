from tkinter import *


def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You don't agree :(")
    # if y.get():
    #     print("You agree!")
    # else:
    #     print("You don't agree :(")
    # if z.get() == "YES":
    #     print("You agree!")
    # else:
    #     print("You don't agree :(")


window = Tk()

x = IntVar()
# y = BooleanVar()
# z = StringVar()

python_photo = PhotoImage(file='Python.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           # variable=y,
                           # onvalue=True,
                           # offvalue=False,
                           # variable=z,
                           # onvalue="YES",
                           # offvalue="NO",
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')

check_button.pack()

window.mainloop()
