import tkinter
import time
window = tkinter.Tk()
window.geometry('50x50')
kleurlist = ['yellow','orange','red','purple','black']
geometrty = ['50x50','100x100','150x150','200x200','250x250']


for x in range (len(kleurlist)):
    window['background']=(kleurlist[x])
    window.geometry(geometrty[x])
    print(6-x)
    time.sleep(1)
    window.update()
window.destroy()
print('BOOM!')

window.mainloop()
