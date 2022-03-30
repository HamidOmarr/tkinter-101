import tkinter as tk
window = tk.Tk()
window.geometry('100x100')
window.title('Hallo')

text = tk.Label(text="Hello, Tkinter",background='blue', foreground='red')
text.pack(pady = 20, padx = 20)
window['background']='yellow'
window.mainloop()