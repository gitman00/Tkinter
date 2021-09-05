from tkinter import *
import tkinter as t
from PIL import ImageTk, Image

wn=t.Tk()
wn.config(background="black")

# function that displays the text inside the canvas
def text():
    global entry,entry2
    canvas.create_text(460,100,fill="royalblue",font=("Roboto Black", 30, "italic bold"),text="Facebook")
    canvas.create_text(150,300,fill="lightblue",font=("Coming Soon", 10, "normal"),text="E-mail :")
    canvas.create_text(150,400,fill="lightblue",font=("Coming Soon", 10, "normal"),text="Password :")
    canvas.create_text(650,500,fill="red",font=("Goodbye", 10, "normal"),text="Forgot password?")
    
    entry=t.Entry(canvas,bg="black",fg="white",justify="center")
    canvas.create_window(530,300,window=entry)
    
    entry2=t.Entry(canvas,bg="black",fg="white",show="x",justify="center")
    canvas.create_window(570,400,window=entry2
    )
    button=t.Button(wn,text="login",bd=10,fg="white",bg="black",activebackground="orange",command=Login)
    canvas.create_window(480,650,window=button)
    
    canvas.update
    
def Login():
      global entry,entry2
      if entry.get()=="manish" and entry2.get() =="manish123":
      	root=t.Tk()
      	label=t.Label(root,text="Welcome Manish !")
      	label.pack()
      	img=ImageTk.PhotoImage(Image.open("facebook.jpg"))
      	label=t.Label(image=img)
      	label.pack()
      	root.mainloop()
      
      	
    # Creating canvas
canvas=t.Canvas(wn,bg="black",height=750,width=900)
a = canvas.create_rectangle(50, 0, 50, 0, fill='red')
canvas.move(a, 20, 20)
canvas.pack()

text()

wn.mainloop()