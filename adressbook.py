from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
w=Tk()
w.title('Adress Book')
w.geometry('700x800+1720+320')
adressbook={}
def opnfl():
    global adressbook
    adressbook.clear()
    listb.delete(0,END)
    file=askopenfile()
    if file is not None:
        adressbook=eval(file.read())
        for i in adressbook:
            listb.insert(END,i)
    else:
        messagebox.showerror('Error','Pick a file')
def svefl():
    files=[('Text Doc','*.txt')]
    file=asksaveasfile(filetypes=files,defaultextension=files)
    if file:
        print(adressbook,file=file)
        listb.delete(0,END)
        adressbook.clear()
    else:
        messagebox.showerror('ERRRR','Not saved')
def updateadd():
    name=e2.get()
    if name=='':
        messagebox.showerror('Error','"NAME" cannot be empty')
    else:
        if name not in adressbook:
            listb.insert(END,name)
        adressbook[name]=(e3.get(),e4.get(),e5.get(),e6.get())
        dele()
def dele():
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
def ed():
    dele()
    selction=listb.curselection()
    if selction:
        e2.insert(0,listb.get(selction))
        detail=adressbook[e2.get()]
        e3.insert(0,detail[0])
        e4.insert(0,detail[1])
        e5.insert(0,detail[2])
        e6.insert(0,detail[3])
    else:
        messagebox.showerror('Error','Select a notion')
def byebye():
    selction=listb.curselection()
    if selction:
        del adressbook[listb.get(selction)]
        listb.delete(selction)
        dele()
    else:
        messagebox.showerror('Error','Make a selection')
def info(Event):
    selction=listb.curselection()
    strvar=''
    if selction: 
        key=listb.get(selction)
        detail=adressbook[key]
        strvar=f'Name: {key}\n'
        strvar+=f'Address: {detail[0]}\n'
        strvar+=f'Mobile: {detail[1]}\n'
        strvar+=f'Email: {detail[2]}\n'
        strvar+=f'DOB: {detail[3]}\n'
    tex=Label(w,text=strvar)
#buttons
b1=Button(w,text='Open',command=opnfl,width=12)
b2=Button(w,text='Edit',command=ed,width=12)
b3=Button(w,text='Delete',command=byebye,width=12)
b4=Button(w,text='Update/Add',command=updateadd,width=12)
b5=Button(w,text='Save',command=svefl,width=12)
#button places
b1.place(x=450,y=20)
b2.place(x=90,y=580)
b3.place(x=190,y=580)
b4.place(x=450,y=580)
b5.place(x=450,y=610)
#list box
listb=Listbox(w,width=50,height=30)
#listbox place
listb.place(x=50,y=80)
listb.bind('<<ListboxSelect>>',info)
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
