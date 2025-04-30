from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
win=Tk()
win.geometry('600x600+1720+720')
login=False
win.wm_attributes('-topmost',2)
win.title('Staff Login')
win.config(background='Black')
button=False

def clear():
    global win
    win.destroy()
def logon():
    global en,login
    txt=en.get()
    pas=ep.get()
    lvl=ce.get()
    if txt=='1234567890' and pas=='password' and lvl=='4':
        child_w= Toplevel(win)
        child_w.geometry('600x600+1720+520')
        child_w.wm_attributes('-topmost',1)
        wel=Label(child_w,text='WELCOME MARION WHEELER',font=('Arial',30,'normal'),bg='black',fg='green')
        wel.pack()
        child_w.config(background='Black')
        login=True
        dic=Button(child_w,text='Access Archives',font=('Arial',20,'normal'),bg='black',fg='green',command=d)
        dic.pack(pady=100)
        s2=Label(child_w,text='''Security Warning: Use of this terminal is covered under the Zeta Corporation Security Agreement. \n Unauthorized use, tampering or recording will be punish under Zeta Corporation's Treason and Terrorism Directive. \n [Article 12, Paragraph 19, Section C]''',bg='black',fg='white',font=('Arial',8,'normal'))
        s2.place(x=15,y=545)
    else:
        messagebox.showerror('Login Denied','Login Denied: Check your Staff ID, Password, or Access level')
#dict
adressbook={}
def d():
    global adressbook
    w=Toplevel(win)
    w.wm_attributes('-topmost',1)
    w.title('Adress Book')
    w.geometry('1000x800+1720+320')
    w.config(background='Black')
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
            messagebox.showerror('Error','Pick an acrchive')
    def svefl():
        files=[('Text Doc','*.txt')]
        file=asksaveasfile(filetypes=files,defaultextension=files)
        if file:
            print(adressbook,file=file)
            listb.delete(0,END)
            adressbook.clear()
        else:
            messagebox.showerror('Error','Not saved')
    def updateadd():
        name=e2.get()
        if name=='':
            messagebox.showerror('Error','"Object" cannot be empty')
        else:
            if name not in adressbook:
                listb.insert(END,name)
            adressbook[name]=(e3.get(),e4.get("1.0", "end-1c"),e5.get(),e6.get())
            dele()
    def dele():
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete('1.0','end')
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
    def info(event):
        c=Toplevel(w)
        c.config(background='black')
        selection=listb.curselection()
        data=''
        if selection:
            key=listb.get(selection)
            data='Object: '+key+'\n'
            details=adressbook[key]
            data+='Class: '+details[0]+'\n'
            data+='Description: '+details[1]+'\n'
            data+='Location: '+details[2]+'\n'
            data+='Date: '+details[3]+'\n'
        l=Label(c,text=data,wraplength=500,font=('Arial',20,'normal'),bg='black',fg='green')
        l.pack()

    bar=Menu(w)
    #1
    file=Menu(bar,tearoff=0)
    bar.add_cascade(label='File',menu=file)
    file.add_command(label='Open file',command=opnfl)
    file.add_separator()
    file.add_command(label='Save',command=svefl)
    file.add_separator()
    file.add_command(label='Exit',command=w.destroy)
    #2
    edit=Menu(bar,tearoff=0)
    bar.add_cascade(label='Edit',menu=edit)
    edit.add_command(label='Edit',command=ed)
    edit.add_command(label='Delete',command=byebye)
    edit.add_separator()
    edit.add_command(label='Update',command=updateadd)
    edit.add_command(label='Add',command=updateadd)
    w.config(menu=bar)
    #list box
    listb=Listbox(w,width=50,height=30)
    #listbox place
    listb.place(x=50,y=80)
    listb.bind('<<ListboxSelect>>',info)
    #bind
    #bagels
    l1=Label(w,text='Archives',font=('Arial',20,'bold'))
    l2=Label(w,text='Object:',width=12)
    l3=Label(w,text='Class:',width=12)
    l4=Label(w,text='Description:',width=12)
    l5=Label(w,text='Location:',width=12)
    l6=Label(w,text='Date:',width=12)
    #bagel placement
    l1.place(x=100,y=20)
    l2.place(x=385,y=100)
    l3.place(x=385,y=150)
    l4.place(x=385,y=200)
    l5.place(x=750,y=200)
    l6.place(x=750,y=250)
    #entrybox
    e2=Entry(w,width=15)
    e3=Entry(w,width=15)
    e4=Text(w,width=25,height=23)
    e5=Entry(w,width=15)
    e6=Entry(w,width=15)
    #entry box place
    e2.place(x=480,y=100)
    e3.place(x=480,y=150)
    e4.place(x=480,y=200)
    e5.place(x=850,y=200)
    e6.place(x=850,y=250)
#label
n=Label(win,text='Staff ID',font=('Arial',20,'normal'),bg='black',fg='white')
n.place(x=50,y=50)
p=Label(win,text='Password',font=('Arial',20,'normal'),bg='black',fg='white')
p.place(x=50,y=120)
s=Label(win,text='''Security Warning: Use of this terminal is covered under the Zeta Corporation Security Agreement. \n Unauthorized use, tampering or recording will be punish under Zeta Corporation's Treason and Terrorism Directive. \n [Article 12, Paragraph 19, Section C]''',bg='black',fg='white',font=('Arial',8,'normal'))
s.place(x=15,y=545)
c=Label(win,text='Access lvl.',font=('Arial',20,'normal'),bg='black',fg='white')
c.place(x=50,y=190)
#entry
en=Entry(win,width=20,font=('Arial',20,'normal'),justify=LEFT)
en.place(x=200,y=50)
ep=Entry(win,show='*',width=20,font=('Arial',20,'normal'))
ep.place(x=200,y=120)
ce=Entry(win,width=4,font=('Arial',20,'normal'))
ce.place(x=200,y=190)
b=Button(win,text='Login',font=('Arial',20,'normal'),bg='black',fg='white',command=logon)
b.place(x=50,y=260)
b2=Button(win,text='Exit',font=('Arial',20,'normal'),bg='black',fg='white',command=clear)
b2.place(x=50,y=320)
mainloop()
