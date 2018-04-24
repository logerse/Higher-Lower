#!/usr/bin/python3

def choose1(event):
	if maincode.checkans(1):
		mlbl.config(text="Yes! That's right!",fg="#34c924")
		maincode.create()
		time.sleep(0.5)
		check()
	else:
		mlbl.config(text="No, it's not.",fg='#f75394')
		obj1.destroy(); obj2.destroy()
		return 1
def choose2(event):
	if maincode.checkans(2):
		mlbl.config(text="Yes! That's right!",fg="#34c924")
		maincode.create()
		time.sleep(0.5)
		mlbl.config(text='HIGHER / LOWER',fg="#485054")
		check()
	else:
		mlbl.config(text="No, it's not.",fg='#f75394')
		obj1.destroy(); obj2.destroy()
def check():
	obj1.config(text=maincode.lastname)
	obj2.config(text=maincode.name)

from tkinter import *
import time
import maincode
root=Tk(); root.title("Higher/Lower")
maincode.startProg()

mainframe=Frame(root,width=1000,height=800,bg='#e0dbd7',bd=100)
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))

mlbl=Label(mainframe,text='HIGHER / LOWER',font="Sans-serif 80",fg="#485054",bg='#e0dbd7')
mlbl.grid(column=2,row=1,sticky=(N,S))

obj1=Button(mainframe,text="-",font="Sans-serif 70",fg="#503457",bg='#e0dbd7')
obj1.grid(column=1,row=2,sticky=W)

obj2=Button(mainframe,text="-",font="Sans-serif 70",fg="#503457",bg='#e0dbd7')
obj2.grid(column=3,row=2,sticky=E)

obj1.bind("<Button-1>",choose1)
obj2.bind("<Button-1>",choose2)

maincode.create()
check()
root.mainloop()
