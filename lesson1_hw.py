from tkinter import *
w=Tk()
w.geometry('600x600+1720+720')
w.title('Staff Login')
w.config(background='Black')
button=False
def clear():
    global w
    w.destroy()
#label
n=Label(w,text='Staff ID',font=('Arial',20,'normal'),bg='black',fg='white')
n.place(x=50,y=50)
p=Label(w,text='Password',font=('Arial',20,'normal'),bg='black',fg='white')
p.place(x=50,y=120)
s=Label(w,text='''Security Warning: Use of this terminal is covered under the Zeta Corporation Security Agreement. \n Unauthorized use, tampering or recording will be punish under Zeta Corporation's Treason and Terrorism Directive. \n [Article 12, Paragraph 19, Section C]''',bg='black',fg='white',font=('Arial',8,'normal'))
s.place(x=15,y=545)
c=Label(w,text='Access lvl.',font=('Arial',20,'normal'),bg='black',fg='white')
c.place(x=50,y=190)
#entry
en=Entry(w,width=20,font=('Arial',20,'normal'),justify=LEFT)
en.place(x=200,y=50)
ep=Entry(w,show='*',width=20,font=('Arial',20,'normal'))
ep.place(x=200,y=120)
b=Button(w,text='Login',font=('Arial',20,'normal'),bg='black',fg='white',command=clear)
b.place(x=50,y=260)
ce=Entry(w,width=4,font=('Arial',20,'normal'))
ce.place(x=200,y=190)
mainloop()
'''w.destroy'''
