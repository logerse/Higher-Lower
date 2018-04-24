#!/usr/bin/python3

class Lables:
	def __init__(self,x=2,y=1,text_="HIGHER\nLOWER"):
		self.obj=Label(mainframe,text=text_,fg="#485054",bg='#e0dbd7',font="Sans-serif 70",bd=80)
		self.obj.grid(column=x,row=y,sticky=(N,S))
	def check(self):
		self.obj.config(text="Yep! +1 Point", fg="#34c924")
		time.sleep(1)
		self.obj.config(text="HIGHER\nLOWER",fg="#485054")
class buttons:
	def __init__(self,x,y,cmmnd,s_,text_="-"):
		self.but=Button(mainframe,text=text_,fg="#503457",bg="#e0dbd7",font="Sans-serif 30",width=9,height=3)
		self.but.grid(column=x,row=y,sticky=s_,padx=50)
		self.but.bind("<Button-1>",cmmnd)
	def check(self,text_=''):
		self.but.config(text=text_)
def chs_1(event):
	if maincode.checkans(1):
		obj1.check()
	maincode.refresh()
	r3fr3sH()
	
def chs_2(event):
	if maincode.checkans(2):
		obj1.check()
	maincode.refresh()
	r3fr3sH()
def r3fr3sH():
	obj2.check(maincode.lastname)
	obj3.check(maincode.name)
from tkinter import *
import time
import maincode
maincode.startProg()
root=Tk(); root.title('Higher-Lower'); root.geometry('1220x600'); root['bg']="#e0dbd7"

#creating mainframe
mainframe=Frame(root,width=1000,height=800,bg='#e0dbd7')
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))

obj1=Lables()
obj2=buttons(1,2,chs_1,W)
obj3=buttons(3,2,chs_2,E)
Points=Lables(2,3,"Points:0")

maincode.create()
r3fr3sH()

root.mainloop()
