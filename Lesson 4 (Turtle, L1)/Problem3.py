from turtle import *

turtle = Turtle()

turtle.pensize(8)
turtle.color('red')
turtle.shape('turtle')
turtle.speed(9)

for x in range(6):
	turtle.forward(100)
	turtle.left(60)



mainloop()