from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
w=Tk()
def opnfl():
    file=askopenfile(mode='r',filetypes=[('Text Doc','*.txt'),('Python','*.py')])
    if file is not None:
        content=file.read()
        print(content)
    else:
        messagebox.showerror('Error','Pick a file')
def svefl():
    files=[('Text Doc','*.txt'),('Python','*.py')]
    file=asksaveasfile(filetypes=files,defaultextension=files)
    if file:
        print(e.get(),file=file)
opn=Button(w,text='Open',command=opnfl)
opn.pack()
sve=Button(w,text='Save',command=svefl)
sve.pack()
e=Entry(w)
e.pack()
mainloop()