from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
w=Tk()
def opnfl():
    file=askopenfile(mode='r',filetypes=[('Text Doc','*.txt'),('Python','*.py')])
    if file is not None:
        l.delete(0,END)
        content=file.readlines()
        for i in content:
            l.insert(END,i)
    else:
        messagebox.showerror('Error','Pick a file')
def svefl():
    files=[('Text Doc','*.txt'),('Python','*.py')]
    file=asksaveasfile(filetypes=files,defaultextension=files)
    if file:
        print(e.get(),file=file)
def delfl():
    sopt=l.curselection()
    if sopt:
        l.delete(sopt)
    else:
        messagebox.showwarning('Oops','There is no current selection')
opn=Button(w,text='Open',command=opnfl)
opn.pack()
sve=Button(w,text='Save',command=svefl)
sve.pack()
e=Entry(w)
e.pack()
dele=Button(w,text='Delete',command=delfl)
dele.pack()
l=Listbox(w,width=60,background='Grey')
l.insert(END,'NO FILE')
l.pack()
mainloop()
#$listbox.insert
#add
