from tkinter import *
import random
from tkinter import messagebox
w=Tk()
w.wm_attributes('-topmost',1)
w.title('Pong')
C=Canvas(w,width=600,height=500,bd=5,highlightthickness=10,bg='black')
C.pack()
v=Canvas.create_text(C,10,400)
C.create_line(300,500,300,0,fill='white')
ballx=0
bally=0
momentumx=0
momentumy=0
speed=5
score1=0
score2=0
move1=0
move2=0
padspeed=4
speeds=[-speed,-speed+1,-speed+2,-speed+3,speed-1,speed,speed-2,speed-3]
random.shuffle(speeds)
momentumx=random.choice(speeds)
momentumy=random.choice(speeds)
def update_scr():
    C.itemconfigure(v,text=f'{score1}:{score2}')
def movement_ball():
    C.move(ball,momentumx,momentumy)
    pos=C.coords(ball)###
    if pos[0]<0:
        momentumx=-momentumx
        score2+=1
        update_scr()
    if pos[2]>C.winfo_width():
        momentumx=-momentumx
        score1+=1
        update_scr()
    if pos[1]<0 or pos[3]>C.winfo_height():
        momentumy=-momentumy
def movement_pad1(event):
    if event.keysym=='w':
        move1=-padspeed
    elif event.keysym=='s':
        move1=+padspeed
#code collison and pad2
#paddlepos
ball=C.create_oval(300,250,280,230,fill='orange')
pad1=C.create_rectangle(15,200,30,300,fill='blue')
pad2=C.create_rectangle(586,200,600,300,fill='red')
C.move(ball,200,200)
mainloop()