from tkinter import *
from tkinter.ttk import *
w=Tk()
w.title('File')
w.geometry('600x600+1720+600')
#menubar
'''bar=Menu(w)
#1
file=Menu(bar,tearoff=0)
bar.add_cascade(label='File',menu=file)
file.add_command(label='New file',command=None)
file.add_separator()
file.add_command(label='Open file',command=None)
file.add_command(label='Open folder',command=None)
file.add_separator()
file.add_command(label='Save',command=None)
file.add_command(label='Save as',command=None)
file.add_separator
file.add_command(label='Exit',command=w.destroy)
#2
edit=Menu(bar,tearoff=0)
bar.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Undo',command=None)
edit.add_command(label='Redo',command=None)
edit.add_separator()
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)
edit.add_separator()
edit.add_command(label='Find',command=None)
edit.add_separator()
edit.add_command(label='Select All',command=None)
w.config(menu=bar)
mainloop()'''

#progressbar
'''progress=Progressbar(w,orient=HORIZONTAL,length=100,mode='determinate')
def bar():
    import time
    progress['value']=20
    w.update_idletasks()
    time.sleep(1)
    progress['value']=40
    w.update_idletasks()
    time.sleep(1)
    progress['value']=60
    w.update_idletasks()
    time.sleep(1)
    progress['value']=80
    w.update_idletasks()
    time.sleep(1)
    progress['value']=100

b=Button(w,text='Render',command=bar)
progress.pack(pady=20)
b.pack(pady=20)
mainloop()
'''

#Spinny numbr
spin=Spinbox(w,from_=0,to=100)
spin.pack()
mainloop()
