from tkinter import *
from gtts import gTTS   
import os
w=Tk()
w.title('Text to speech')
w.geometry('700x800+1720+320')
def audio():
    file=gTTS(text=E.get(),lang='es',slow=False)
    file.save('wave.wav')
    os.system('wave.wav')
L=Label(w,text='Text to speech',font=('Normal',30))
E=Entry(w,width=30,font=('Normal',30))
B=Button(w,text='Convert',font=('Normal',30),command=audio)
L.pack()
E.pack()
B.pack()
mainloop()
