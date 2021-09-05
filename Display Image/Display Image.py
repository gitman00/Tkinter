import turtle as t

screen=t.Screen()
screen.bgcolor("royalblue")
#screen.tracer(0)

screen.register_shape("man.gif")

def Player():
	player=t.Turtle()
	player.shape("man.gif")
	player.shapesize(10)
	player.left(90)
	player.color("red", "black")
	
def update():
	screen.mainloop()	
	
Player()
update()