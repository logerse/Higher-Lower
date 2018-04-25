#!/usr/bin/python3

#-------Класс надписей(очки, главная надпись)------------

class Lables:
	def __init__(self,x=2,y=1,text_="HIGHER\nLOWER"):
		self.obj=Label(mainframe,text=text_,fg="#485054",bg='#e0dbd7',font="Sans-serif 70",bd=80)
		self.obj.grid(column=x,row=y,sticky=(N,S))
	#   Изменение основных свойств надписи
	def check(self,points,text_='',color=""):
		if text_=='':
			self.obj.config(text="Points:"+points)
		else:
			self.obj.config(text=text_,fg=color)
			if text_[0]=='P':
				self.obj.config(font="Sans-serif 30")
			root.geometry('580x500')
	#   Удаление виджета
	def dlt(self):
		self.obj.destroy()

#--------Класс кнопок (вариант ответа №1, вариант ответа №2)----------

class buttons:
	def __init__(self,x,y,cmmnd,s_,text_="-"):
		self.but=Button(mainframe,text=text_,fg="#503457",bg="#e0dbd7",font="Sans-serif 30",width=9,height=3)
		self.but.grid(column=x,row=y,sticky=s_,padx=50)
		self.but.bind("<Button-1>",cmmnd)
	#   Изменение надписи на кнопках
	def check(self,text_=''):
		self.but.config(text=text_)
	#   Удаление виджета
	def dlt(self):
		self.but.destroy()

#--------Действия в случае ошибочного ответа-----------

def miss():
	global points
	obj1.check(0,"You lose",'#ff335c')
	obj2.dlt()
	obj3.dlt()
	Points.check(0,"Points:"+str(points),'#ff335c') 

#-------Проверка ответа (вариант ответа №1)------------

def chs_1(event):
	global points
	if maincode.checkans(1):
		points+=1
	else:
		miss()
		return 0	
	maincode.refresh()
	r3fr3sH()

#-------Проверка ответа (вариант ответа №2)---------

def chs_2(event):
	global points
	if maincode.checkans(2):
		points+=1
	else:
		miss()
		return 0
	maincode.refresh()
	r3fr3sH()

#-------Обновление вариантов и количества очков--------

def r3fr3sH():
	Points.check(str(points))
	obj2.check(maincode.lastname)
	obj3.check(maincode.name)

#-------import tkinter-------

from tkinter import *

#-------import code(core)-------

import maincode

#----------------------------

points = 0

#-------Генерация списка вариантов--------

maincode.startProg()

#-------Создание основного окна-------

root = tkinter.Tk()
root.title('Higher-Lower'); root.geometry('1220x600'); root['bg']="#e0dbd7"

#-------Создание основного фрейма--------

mainframe=tkinterFrame(root,width=1000,height=800,bg='#e0dbd7')
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))

#------Создание объектов--------

obj1=Lables()
obj2=buttons(1,2,chs_1,W)
obj3=buttons(3,2,chs_2,E)
Points=Lables(2,2,"Points:"+str(points))

#-------Генерация и присваивание вариантов виджетам--------

maincode.create()
r3fr3sH()

#------------------------------
root.mainloop()
