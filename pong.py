from tkinter import *
import random
from tkinter import messagebox
import time
w=Tk()
w.wm_attributes('-topmost',1)
w.title('Pong')
C=Canvas(w,width=600,height=500,bd=5,highlightthickness=10,bg='black')
C.pack()
v=C.create_text(300,50,font=('Arial',10,'normal'),text='0:0',fill='white')
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
ball=C.create_oval(300,250,280,230,fill='orange')
pad1=C.create_rectangle(15,200,30,300,fill='blue')
pad2=C.create_rectangle(586,200,600,300,fill='red')
C.move(ball,200,200)
def update_scr():
    C.itemconfigure(v,text=f'{score1}:{score2}')
def movement_ball():
    global momentumx, momentumy
    C.move(ball,momentumx,momentumy)
    pos=C.coords(ball)###
    if pos[0]<0:
        global score2
        momentumx=-momentumx
        score2+=1
        update_scr()
    if pos[2]>C.winfo_width():
        global score1
        momentumx=-momentumx
        score1+=1
        update_scr()
    if pos[1]<0 or pos[3]>C.winfo_height():
        momentumy=-momentumy
    if collide(pad1,pos):
        momentumx=speed
    if collide(pad2,pos):
        momentumx=speed
def movement_pad1(event):
    global move1
    if event.keysym=='w':
        move1=-padspeed
    elif event.keysym=='s':
        move1=+padspeed
def movement_pad2(event):
    global move2
    if event.keysym=='i':
        move2=-padspeed
    elif event.keysym=='j':
        move2=+padspeed
def collide(pad,bpos):
    pos=C.coords(pad)
    if bpos[1]>=pos[1] and bpos[1]<=pos[3]:
        if bpos[0]<=pos[2] and bpos[2]>=pos[0]:
            return True
        elif bpos[2]>=pos[0] and bpos[0]<=pos[2]:
            return True
    return False
def padbor(pad,ymove):
    C.move(pad,0,ymove)
    pos=C.coords(pad)
    if pos[1]<=0:
        ymove=0
    if pos[3]>=C.winfo_height():
        ymove=0
    return ymove
C.bind_all('w',movement_pad1)
C.bind_all('s',movement_pad1)
C.bind_all('i',movement_pad2)
C.bind_all('j',movement_pad2)
#code collison and pad2
while True:
    if score1==10 or score2==10:
        messagebox.showinfo("Game Over",f'Score is {score1}:{score2}')
        break
    movement_ball()
    move1=padbor(pad1,move1)
    move2=padbor(pad2,move2)
    C.move(pad1,0,move1)
    C.move(pad2,0,move2)
    w.update_idletasks()
    w.update()
    time.sleep(0.05)
#paddlepos
mainloop()
