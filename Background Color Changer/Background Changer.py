from tkinter import *
import tkinter as t
root=t.Tk()
root.config(background="royalblue")

def blue():
	root.config(background='blue')	
def green():
	root.config(background='green')
def black():
	root.config(background='black')
def white():
	root.config(background='white')
def yellow():
	root.config(background='yellow')
def red():
	root.config(background='red')
def pink():
	root.config(background='pink')		

blue_button=t.Button(root,text="Blue",command=blue,fg="blue").pack()
green_button=t.Button(root,text="Green",command=green,fg="green").pack()
red_button=t.Button(root,text="Red",fg="red",command=red).pack()
yellow_button=t.Button(root,text="Yellow",command=yellow,fg="yellow").pack()
black_button=t.Button(root,text="Black",command=black,fg="black").pack()
white_button=t.Button(root,text="White",command=white,fg="white").pack()
pink_button=t.Button(root,text="Pink",command=pink,fg="pink").pack()
root.mainloop()