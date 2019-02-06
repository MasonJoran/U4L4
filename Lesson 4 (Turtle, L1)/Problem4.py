from turtle import *

turtle = Turtle()
turtle1 = Turtle()

turtle.pensize(8)
turtle.color('red')
turtle.shape('turtle')
turtle.speed(9)

turtle1.pensize(8)
turtle1.color('blue')
turtle1.shape('turtle')
turtle1.speed(9)

for x in range(3):
	turtle.forward(100)
	turtle.left(120)

turtle1.backward(150)
turtle1.circle(75)

mainloop()