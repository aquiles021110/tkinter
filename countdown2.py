from tkinter import *
from tkinter import messagebox
import time
w=Tk()
w.title('Countdown')
hour=StringVar()
min=StringVar()
sec=StringVar()
hour.set('0')
min.set('0')
sec.set('0')
pause=False
timerid=None
running=False
def buttonp():
    global pause,timerid
    pause=not pause
    if not pause:
        if timerid:
            w.after_cancel(timerid)
        simplify()
def count():
    global pause,running,totalsec,timerid
    if running:
        return
    running=True
    pause=False
    totalsec=int(hour.get())*3600+int(min.get())*60+int(sec.get())
    simplify()
def simplify():
    global pause,totalsec,timerid,running
    if totalsec>0:
        if not pause:
            totalsec-=1
            m,s=divmod(totalsec,60)
            h,m=divmod(m,60)
            hour.set(h)
            min.set(m)
            sec.set(s)
        timerid=w.after(1000,simplify)
    elif totalsec==0:
        messagebox.showinfo('Done',"time's up!")
        running=False  
entryh=Entry(w,width=5,textvariable=hour)
entryh.grid(row=0,column=0)
entrym=Entry(w,width=5,textvariable=min)
entrym.grid(row=0,column=1)
entrys=Entry(w,width=5,textvariable=sec)
entrys.grid(row=0,column=2)
button=Button(w,text='Start Countdown',command=count)
button.grid(row=1,column=1)
button2=Button(w,text='Stop/Start',command=buttonp)
button2.grid(row=2,column=1)
mainloop()
