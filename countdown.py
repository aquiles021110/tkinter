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
def buttonp():
    global pause
    if pause==True:
        pass
    elif pause==False:
        pause=True
def count():
    global pause
    totalsec=int(hour.get())*3600+int(min.get())*60+int(sec.get())
    while totalsec>0:
        if pause==False:
            m,s=divmod(totalsec,60)
            h=0
            if m>60:
                h,m=divmod(m,60)
            hour.set(h)
            min.set(m)
            sec.set(s)
            w.update()
            time.sleep(1)
            if totalsec==0:
                messagebox.showinfo('Done',"time's up!")
            totalsec-=1
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