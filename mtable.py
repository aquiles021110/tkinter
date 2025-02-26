from tkinter import *
w=Tk()
w.title('Multiply')
tablefinal=''
def multipla(nmum):
    global tablefinal
    line0=f'{nmum} X 0 = {nmum*0}'
    line1=f'{nmum} X 1 = {nmum*1}'
    line2=f'{nmum} X 2 = {nmum*2}'
    line3=f'{nmum} X 3 = {nmum*3}'
    line4=f'{nmum} X 4 = {nmum*4}'
    line5=f'{nmum} X 5 = {nmum*5}'
    line6=f'{nmum} X 6 = {nmum*6}'
    line7=f'{nmum} X 7 = {nmum*7}'
    line8=f'{nmum} X 8 = {nmum*8}'
    line9=f'{nmum} X 9 = {nmum*9}'
    line10=f'{nmum} X 10 = {nmum*10}'
    tablefinal=f'{line0}\n{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}\n{line8}\n{line9}\n{line10}'
def tabel():
    c=Tk()
    c.config(bg='Grey')
    fetchy=int(e.get())
    multipla(fetchy)
    text=Text(c,font='Consolas 10',wrap='none',height=15,width=34)
    text.insert('1.0',tablefinal)
    text.config(state='disabled')
    text.pack()
    c.mainloop()
t=Label(w,text='Multiplication Table',bg='gray',font=('Arial',25,'normal'))
l=Label(w,text='Enter number',font=('Arial',15,'normal'))
e=Entry(w,width=5,font=('Arial',15,'normal'))
b1=Button(w,text='Enter',command=tabel)
be=Button(w,text='Exit',command=w.destroy)
t.pack()
l.pack()
e.pack()
b1.pack()
be.pack()
mainloop()