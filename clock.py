import time,random
from tkinter import *
w=Tk()
w.title('Clock')
colour=['white','black','red','green','blue']
dtime=Label(w,font=('arial',40))
dtime.pack()
def refresh():
    currenttime=time.strftime('%H:%M:%S')
    dtime.config(text=currenttime,fg=random.choice(colour),bg=random.choice(colour))
    dtime.after(1000,refresh)
refresh()
mainloop()