from turtle import *

turtle = Turtle()

screen = Screen()
screen.bgcolor('blue')

turtle.pensize(8)
turtle.color('red')
turtle.shape('turtle')
turtle.speed(9)


for x in range(12):
	turtle.forward(200)
	turtle.left(120)
	turtle.left(30)

turtle.penup()
turtle.backward(100)
turtle.pendown()

for x in range(12):
	turtle.forward(200)
	turtle.left(120)
	turtle.left(30)

turtle.penup()
turtle.backward(100)
turtle.pendown()

for x in range(12):
	turtle.forward(200)
	turtle.left(120)
	turtle.left(30)


mainloop()