import time
from tkinter import *
from tkinter.ttk import *


def start():
    GB = 500
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download) + "/" + str(GB) + " GB completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent)
percent_label.pack()

task_label = Label(window, textvariable=text)
task_label.pack()

button = (Button(window, text="download", command=start))
button.pack()

window.mainloop()
