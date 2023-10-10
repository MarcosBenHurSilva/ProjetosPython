from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Usuario\\PycharmProjects\\helloWorld",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    # filetext = input("Enter some text I guess: ") # use this if you want to use console window
    file.write(filetext)
    file.close()


window = Tk()
button = Button(text='save', command=saveFile)
button.pack()
text = Text(window,
            bg='black',
            font=("Arial", 20),
            fg='light green'
            )
text.pack()

window.mainloop()
