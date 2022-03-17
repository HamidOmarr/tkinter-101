import tkinter
import time
window = tkinter.Tk()
window.geometry('0x0')
def achtergrondGeel():
    window.geometry('100x100')
    window['background']='yellow'
    print ('5')
def achtergrondOrange():
    window.geometry('150x150')
    window['background']='orange'
    print ('4')
def achtergrondRood():
    window.geometry('200x200')
    window['background']='red' 
    print ('3')
def achtergrondPaars():
    window.geometry('250x250')
    window['background']='purple'
    print ('2')
def achtergrondZwart():
    window.geometry('300x300')
    window['background']='black'
    print ('1')
def WindowBoom():
    window.destroy()
    print('BOOM!')

window.after(1000,achtergrondGeel)
window.after(2000,achtergrondOrange)
window.after(3000,achtergrondRood)
window.after(4000,achtergrondPaars)
window.after(5000,achtergrondZwart)
window.after(6000,WindowBoom)

window.mainloop()
