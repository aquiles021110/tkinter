from tkinter import *
import speech_recognition as sr 
import os
from tkinter.filedialog import *
from tkinter import messagebox
w=Tk()
w.title('Speech to text')
w.geometry('1000x500+1720+320')
def transl():
    audio=sr.Recognizer()
    with sr.Microphone() as source:
        print('Recording...')
        hear=audio.listen(source)
        try:
            text=audio.recognize_google(hear,language='fr-FR')
        except:
            text='Error, idk'
        E.delete(1.0,END)
        E.insert(END,text)
def svefl():
    files=[('Text Doc','*.txt')]
    file=asksaveasfile(filetypes=files,defaultextension=files)
    if file:
        print(E.get(1.0,END),file=file)
    else:
        messagebox.showerror('ERRRR','Not saved')
L=Label(w,text='Voice Notepad',font=('Normal',30))
E=Text(w,width=30)
B=Button(w,text='Start Recording',font=('Normal',30),command=transl)
B2=Button(w,text='Save file as txt.',font=('Normal',30),command=svefl)
L.grid(row=0,column=1)
E.grid(column=1,row=1)
B.grid(row=1,column=0)
B2.grid(row=1,column=2)
mainloop()
