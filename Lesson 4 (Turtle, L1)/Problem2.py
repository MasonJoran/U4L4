from turtle import *

turtle = Turtle()

turtle.pensize(8)
turtle.color('red')
turtle.shape('turtle')
turtle.speed(9)

for x in range(4):
	turtle.forward(200)
	turtle.right(90)

mainloop()