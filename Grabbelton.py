import tkinter as tk
import random
window = tk.Tk()
RandomLijst = ['1','2','3','4','5','6','7','8','9','10']
def RandomGrab():
    if(button['text']=='Grab!'):
        b = random.choice(RandomLijst)
        button['text']='Grabbed!'
        print(b)
        RandomLijst.remove(b)
    else:
        print(RandomLijst)
        button['text']=('Grab!')

window['background']='teal'
button = tk.Button(text='Grab!', foreground='black', command=RandomGrab)
button.pack(pady = 20, padx = 20)
window.mainloop()