import turtle
import random

h = turtle.Turtle()
h.speed(1000)

#Function
 
    
def makeFlake(x,y):
    h.penup()
    h.setposition(x,y)
    h.color("cyan")
    for i in range(50):
        h.setheading(90)
        h.forward(5)
        h.backward(2.5)
        h.setheading(270)
        h.forward(2.5)
        h.backward(5)
        h.penup()
        h.left(45)
        h.forward(25)
        h.setheading(45)
        h.pendown()

def makeSnow():
    makeFlake(-325,323)
    makeFlake(-300,312)
    makeFlake(-275,306)
    makeFlake(-250,297)
    makeFlake(-225,305)
    makeFlake(-200,289)

#MAIN
h.penup()
makeSnow()
h.pendown()
