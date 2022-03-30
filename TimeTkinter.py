import tkinter
from tkinter.ttk import *

from time import strftime

window = tkinter.Tk()
window.title('Clock')

def toontijd():
	tijd = strftime('%H:%M:%S')
	Labeltime.config(text = tijd)
	Labeltime.after(1000, toontijd)

Labeltime = Label(window, font = ('Courier', 50, 'italic'),
			background = 'blue',
			foreground = 'black')

Labeltime.pack()
toontijd()

window.mainloop()

