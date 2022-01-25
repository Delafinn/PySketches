from turtle import Turtle , Screen
import random
from random import randint


def random_colors():
    r1 = randint(0,255)
    r2 = randint(0,255)
    r3 = randint(0,255)
    random_colors = [r1,r2,r3]
    return tim.color(random_colors)


#main

scr = Screen()
scr.colormode(255)
scr.listen()
scr.title("PySketches")


tim = Turtle()
tim.shape("circle")
tim.speed("fastest")
tim.width(3)
tim.shapesize(1,1,0)


def moveup():
    tim.setheading(90)
    tim.fd(10)

def movedown():
    tim.setheading(270)
    tim.fd(10)

def moveright():
    tim.setheading(0)
    tim.fd(10)

def moveleft():
    tim.setheading(180)
    tim.fd(10)

def penup():
    tim.penup()

def pendown():
    tim.pendown()

def clear():
    tim.clear()

def RetroTheme():
    return scr.bgcolor("gray")

scr.onkey(key = "Up", fun = moveup)
scr.onkey(key = "Down", fun = movedown)
scr.onkey(key = "Right", fun = moveright)
scr.onkey(key = "Left", fun = moveleft)
scr.onkey(key = "z", fun = penup)
scr.onkey(key = "x", fun = pendown)
scr.onkey(key = "c", fun = random_colors)
scr.onkey(key = "space", fun =clear)
scr.onkey(key = "r", fun = RetroTheme)

scr.exitonclick()



"""Welcome to PySketches!
Hello World! Welcome to PySketches!
Pysketches is a python etch n sketch app that has multiple colors for drawing,
the ability to pick up the pen so you don’t have to sketch over your work.
and the abilty to put the pen back on the canvas to continue your drawing. as well as the abilty to clear the canvas.
How To
PySketches uses several inputs. arrow keys will move the sketcher,
“Z” will pull your pen off the canvas so you can move around the canvas without drwaing.
“X” allows you to put the pen back on the canvas to continue drawing.
“C” allows you the change the color (keep in mind the colors are randomly generated.
“Spacebar” will clear the canvas.
Lastly, clicking on the Canvas will exit the python program."""
