from tkinter import *
import tkinter as t
from PIL import ImageTk, Image


wn=t.Tk()
wn.config(background="black")
exp=' '

def job():
	window=t.Tk()
	window.title('@ MANISH CALC')
		
	def add(value):
		global exp
		exp  +=  value
		display.config(text=exp)
		
	
	def clear():
		global exp
		exp=" "
		display.config(text=exp)
	
	def calculation():
		global exp
		result=""
		if exp != "":
			try:
				result=eval(exp)
				
				
			except:
				result="E--R--R--O--R"
				exp=""
			display.config(text=result)		

	
			
	# displaying result
	display=t.Button(window,text="",bg='gray',font=("Roboto Black" ,8),activebackground="gray",fg='white',height=5,width=30,activeforeground="white")
	display.grid(row=0, column=0, columnspan=4)
	
	# creating buttons
	button_7=t.Button(window,text="7",bd=10,activebackground="orange",bg="white",font=("Dancing Script", 10),activeforeground='white',width=3,height=3,command=lambda: add('7')).grid(row=1, column=0)	
	button_8=t.Button(window,text="8",bd=10,activeforeground='white',width=3,height=3,font=("Dancing Script", 10),activebackground="orange",bg="white",command=lambda: add('8')).grid(row=1, column=1)	
	button_9=t.Button(window,text="9",bd=10,activeforeground='white',width=3,height=3,font=("Dancing Script", 10),activebackground="orange",bg="white",command=lambda: add('9')).grid(row=1, column=2)	
	button_op1=t.Button(window,text="/",bd=10,activeforeground='white',width=3,font=("Roboto Black", 10),activebackground="orange",bg="white",height=3,command=lambda: add('/')).grid(row=1, column=3)	
	button_4=t.Button(window,text="4",bd=10,activeforeground='white',width=3,height=3,font=("Dancing Script", 10),activebackground="orange",bg="white",command=lambda: add('4')).grid(row=2, column=0)	
	button_5=t.Button(window,text="5",bd=10,activeforeground='white',width=3,height=3,font=("Dancing Script", 10),activebackground="orange",bg="white",command=lambda: add('5')).grid(row=2, column=1)	
	button_6=t.Button(window,text="6",bd=10,activeforeground='white',width=3,height=3,font=("Dancing Script", 10),activebackground="orange",bg="white",command=lambda: add('6')).grid(row=2, column=2)
	button_op2=t.Button(window,text="*",bd=10,activeforeground='white',width=3,height=3,activebackground="orange",font=("Roboto Black", 10),bg="white",command=lambda: add('*')).grid(row=2, column=3)	
	button_1=t.Button(window,text="1",font=("Dancing Script", 10),bd=10,activeforeground='white',width=3,height=3,activebackground="orange",bg="white",command=lambda: add('1')).grid(row=3, column=0)	
	button_2=t.Button(window,text="2",bd=10,activeforeground='white',width=3,height=3,font=("Dancing Script", 10),activebackground="orange",bg="white",command=lambda: add('2')).grid(row=3, column=1)	
	button_3=t.Button(window,text="3",bd=10,activeforeground='white',width=3,height=3,font=("Dancing Script", 10),activebackground="orange",bg="white",command=lambda: add('3')).grid(row=3, column=2)	
	button_op3=t.Button(window,text="+",bd=10,activeforeground='white',width=3,font=("Roboto Black", 10),height=3,activebackground="orange",bg="white",command=lambda: add('+')).grid(row=3, column=3)	
	button_clear=t.Button(window,text="C",bd=10,activeforeground='white',width=3,font=("Roboto Black", 10),height=3,activebackground="red",bg="red",command=lambda: clear()).grid(row=4, column=0)	
	button_zero=t.Button(window,text="0",bd=10,activeforeground='white',width=3,font=("Roboto Black", 10),height=3,activebackground="orange",bg="white",command=lambda: add('0')).grid(row=4, column=1)
	button_point=t.Button(window,text=" . ",bd=10,activeforeground='white',width=3,font=("Roboto Black", 10),height=3,activebackground="orange",bg="white",command=lambda: add('.')).grid(row=4, column=2)	
	button_subtract=t.Button(window,text="-",bd=10, activeforeground='white',width=3,font=("Roboto Black", 10),height=3,activebackground="orange",bg="white",command=lambda: add('-')).grid(row=4, column=3)	
	
	calculating=t.Button(window,text="=",bg='lightblue',activebackground='lightblue',font=("Roboto Black", 8, "italic bold"),activeforeground='red',fg='red',bd=10,width=30,height=3,command=lambda: calculation()).grid(row=6, column=0, columnspan=4)
	
	
	window.mainloop()
	
def New():
	Newwindow=t.Tk()	
	Newwindow.title('Window')
	
def Open():
	top=t.Tk()
	top.title('files')
	List= Listbox(top,bd=20,fg='white',bg="black")
	List.insert(1, "• abc.py")
	List.insert(2, "• Perl.py")
	List.insert(3, "• Cars.py")
	List.insert(4, "• space.py")
	List.insert(5, "• war.py")
	List.insert(6, "• Ruby.py")
	List.pack()
	
	top.mainloop()


	

	
def Save_as():
	saveas=t.Tk()
	
	L1 = Label(saveas, text="File Name : ",font=("Roboto Black", 10)).pack( side = LEFT)
	E1 = Entry(saveas, bd =5)
	E1.pack(side = LEFT)
	bbb=t.Button(saveas,text="save",command=Save)
	bbb.pack(anchor='center')
	
	saveas.mainloop()
	
def Save():
	S=t.Tk()
	bbb=t.Button(S,text="Save",command=wn.quit).pack()
	S.mainloop()
	
menubar = Menu(wn,bg="blue",fg="white",activebackground="blue" ,font=("Dancing Script", 10),activeforeground="yellow",bd=10)
filemenu = Menu(menubar, tearoff=0,activebackground="yellow",bg="white",fg="black")
filemenu.add_command(label="New",command=New)
filemenu.add_command(label="Open",command=Open)
filemenu.add_command(label="Save",command=Save)
filemenu.add_command(label="Save as……",command=Save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=wn.quit)
menubar.add_cascade(label="File",menu=filemenu)

editmenu = Menu(menubar, tearoff=0,activebackground="yellow",bg="white",fg="black")
editmenu.add_command(label="Cut",command=New)
editmenu.add_command(label="Copy",command=New)
editmenu.add_command(label="Paste",command=New)
editmenu.add_command(label="Select all",command=New)
editmenu.add_separator()
editmenu.add_command(label="Delete",command=New)
menubar.add_cascade(label="Edit",menu=editmenu)		
	
wn.config(menu=menubar)







display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓   ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()

# DISPLAYING IMAGE
img=ImageTk.PhotoImage(Image.open("Calculator.png"))
label=t.Label(image=img)
label.pack()	

display=t.Label(wn,text="Click The Below Button ",font=("Dancing Script", 12),fg='lightblue',bg="black").pack()
display=t.Label(wn,text="To Open Calculator",font=("Dancing Script", 12),fg='orange',bg="black").pack()
C=t.Button(wn, text='Calculator',bd=20,font=("Roboto Black", 20),bg="red",activebackground="blue",fg="white",command=job).pack(anchor='n')

display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ↓ ",fg='red',bg="black").pack()

display=t.Label(wn,text="**********-THIS CALCULATOR IS MADE**********",fg='white',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text="↓ ↓ ",fg='red',bg="black").pack()
display=t.Label(wn,text=" By ",fg='white',bg="black",font=("Dancing Script", 10)).pack()
display=t.Label(wn,text="↓",fg='red',bg="black").pack()

display=t.Label(wn,text="<<<<<<<<<< Mr.Manish Ghimire >>>>>>>>",font=("Dancing Script", 15),fg='lime',bg="black").pack()



wn.mainloop()