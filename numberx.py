from tkinter import *
from tkinter.ttk import *
w=Tk()
w.title('Multiply')
title=Label(w,text='Mutiplication Table')
title.grid(row=0,column=1)
l=Label(w,text='Number and range=')
l.grid(row=1,column=0)
###
def tablegen():
    display=''
    for u in range(rnum.get()+1):
        display+=f'{num.get()} X {u} = {num.get()*u}\n'
    table.config(text=display)
###
num=IntVar()
combo=Combobox(w,textvariable=num,width=5)
combo['values']=tuple(range(1,101))
combo.grid(row=1,column=1)
###
rnum=IntVar()
radio1=Radiobutton(w,text='10',variable=rnum,value=10)
radio2=Radiobutton(w,text='20',variable=rnum,value=20)
radio1.grid(row=1,column=2,padx=20)
radio2.grid(row=2,column=2,padx=20)
###
gen=Button(w,text='Generate',command=tablegen)
gen.grid(row=3,column=1)
###
table=Label(w)
table.grid(row=4,column=1)
###
mainloop()