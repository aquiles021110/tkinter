from tkinter import *
from tkinter import messagebox
import random
w=Tk()
randnumber=random.randint(0,20)
w.title('Number guessing game')
l1=Label(w,text='Welcome to the game')
l1.pack(pady=10)
l2=Label(w,text="What's your name?")
l2.pack()
def button1():
    name=e1.get()
    messagebox.showinfo('Hi',f'Hello {name}, i am thinking of a number from 0 and 20')
f2=Frame(w)
f2.pack()
e1=Entry(f2,width=12)
e1.grid(row=0,column=0,padx=29)
b1=Button(f2,text='OK',command=button1)
b1.grid(row=0,column=1)
f=Frame(w)
f.pack()
def button2():
    num=int(e2.get())
    if num==randnumber:
        messagebox.showinfo('Correct','Good job, that is the correct number!')
    elif num>randnumber:
        messagebox.showinfo('Lower','The number that i am thinking of is lower than that')
    elif num<randnumber:
        messagebox.showinfo('Higher','The number i am thinking of is higher than that')
l3=Label(f,text='Your Guess:')
l3.grid(row=0,column=0)
e2=Entry(f,width=5)
e2.grid(row=0,column=1,padx=16)
b2=Button(f,text='OK',command=button2)
b2.grid(row=0,column=2)
mainloop()
