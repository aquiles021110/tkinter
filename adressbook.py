from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
w=Tk()
w.title('Adress Book')
w.geometry('700x800+1720+320')
#buttons
b1=Button(w,text='Open',command=None,width=12)
b2=Button(w,text='Edit',command=None,width=12)
b3=Button(w,text='Delete',command=None,width=12)
b4=Button(w,text='Update/Add',command=None,width=12)
b5=Button(w,text='Save',command=None,width=12)
#button places
b1.place(x=450,y=20)
b2.place(x=90,y=580)
b3.place(x=190,y=580)
b4.place(x=)
#list box
listb=Listbox(w,width=50,height=30)
#listbox place
listb.place(x=50,y=80)
#bagels
l1=Label(w,text='Address Book',font=('Arial',20,'bold'))
l2=Label(w,text='Name:',width=12)
l3=Label(w,text='Address:',width=12)
l4=Label(w,text='Mobile:',width=12)
l5=Label(w,text='Email:',width=12)
l6=Label(w,text='DOB:',width=12)
#bagel placement
l1.place(x=100,y=20)
l2.place(x=385,y=100)
l3.place(x=385,y=150)
l4.place(x=385,y=200)
l5.place(x=385,y=250)
l6.place(x=385,y=300)
#entrybox
e2=Entry(w,width=15)
e3=Entry(w,width=15)
e4=Entry(w,width=15)
e5=Entry(w,width=15)
e6=Entry(w,width=15)
#entry box place
e2.place(x=480,y=100)
e3.place(x=480,y=150)
e4.place(x=480,y=200)
e5.place(x=480,y=250)
e6.place(x=480,y=300)
#closeloop
mainloop()