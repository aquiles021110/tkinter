from tkinter import *
from tkinter import messagebox
class Tictactoe():
    def __init__(self,win):
        self.win=win
        self.win.title('Tic Tac Toe')
        self.currentplayer='x'
        self.buttons=[[None for i in range(3)]for j in range(3)]
        print(self.buttons)
        self.widgets()
    def widgets(self):
        for r in range(3):
            for c in range(3):
                b=Button(self.win,text='',font=('Bold',40),width=5,height=2,command=lambda x=r,y=c:self.click(x,y))
                b.grid(row=r,column=c)
                self.buttons[r][c]=b
    def click(self,i,j):
        if self.buttons[i][j]['text']=='' and not self.winner():
            self.buttons[i][j]['text']=self.currentplayer
            if self.winner():
                messagebox.showinfo('WIN',f'{self.currentplayer} has won.')
            elif self.draw():
                messagebox.showinfo('DRAW','The game has ended in a Draw')
            else:
                if self.currentplayer=='X':
                    self.currentplayer='O'
                else:
                    self.currentplayer='X'
    def winner(self):
        for i in range(3):
            if self.buttons[i][0]['text']==self.buttons[i][1]['text']==self.buttons[i][2]['text']!='':
                return True
        for j in range(3):
            if self.buttons[0][j]['text']==self.buttons[1][j]['text']==self.buttons[2][j]['text']!='':
                return True
        if self.buttons[0][0]['text']==self.buttons[1][1]['text']==self.buttons[2][2]['text']!='':
            return True
        if self.buttons[0][2]['text']==self.buttons[1][1]['text']==self.buttons[2][0]['text']!='':
            return True
        return False
    def draw(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text']=='':
                    return False
        return True
win=Tk()
Tictactow=Tictactoe(win)
mainloop()
