from tkinter import *
import random
w=Tk()
w.title('Rock Paper Scissors')
scorep=0
scorec=0
options=['rock','paper','scissors']
def tie():
    global scorec,scorep
    t.config(text='Tie',fg='Grey')
    l6.config(text='Player Score: '+str(scorep))
    l7.config(text='Computer Score: '+str(scorec))
def win():
    global scorec,scorep
    t.config(text='Win',fg='Green')
    scorep=scorep+1
    l6.config(text='Player Score: '+str(scorep))
    l7.config(text='Computer Score: '+str(scorec))
def lose():
    global scorec,scorep
    t.config(text='Lose',fg='Red')
    scorec=scorec+1
    l6.config(text='Player Score: '+str(scorep))
    l7.config(text='Computer Score: '+str(scorec))
def wol(player):
    choicecom=random.choice(options)
    l4.config(text='You selected:'+player)
    l5.config(text='Computer Selected:'+choicecom)
    if player==choicecom:
        tie()
    elif player==options[0] and choicecom==options[1]:
        lose()
l1=Label(w,text='Rock Paper Scissors')
l1.pack()
t=Label(w,font=('arial'))
t.pack()
f2=Frame(w)
f2.pack()
l2=Label(f2,text='Your options:')
l2.grid(row=0,column=0)
b1=Button(f2,text='Rock',bg='blue',fg='black',command=None)
b1.grid(row=1,column=1,padx=10)
b2=Button(f2,text='Paper',bg='grey',fg='black',command=None)
b2.grid(row=1,column=2,padx=10)
b3=Button(f2,text='Scissors',bg='pink',fg='black',command=None)
b3.grid(row=1,column=3,padx=10)
l3=Label(f2,text='Score:')
l3.grid(row=2,column=0)
f=Frame(w)
f.pack()
l4=Label(f,text='You selected:')
l4.grid(column=0,row=0)
l5=Label(f,text='Computer Selected:')
l5.grid(column=0,row=1)
l6=Label(f,text='Player Score:')
l6.grid(column=1,row=0)
l7=Label(f,text='Computer Score:')
l7.grid(column=1,row=1)
mainloop()
