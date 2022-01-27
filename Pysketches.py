import random
import turtle


def random_colors():
    r1 = random.randint(0, 255)
    r2 = random.randint(0, 255)
    r3 = random.randint(0, 255)
    colors = [r1, r2, r3]
    tim.color(colors)


canvas = turtle.Screen()
canvas.colormode(255)
canvas.listen()
canvas.title("PySketches")

tim = turtle.Turtle()
tim.shape("circle")
tim.speed("fastest")
tim.width(3)
tim.shapesize(0.5, 0.5, 0)


def move_up():
    tim.setheading(90)
    tim.fd(10)


def move_down():
    tim.setheading(270)
    tim.fd(10)


def move_right():
    tim.setheading(0)
    tim.fd(10)


def move_left():
    tim.setheading(180)
    tim.fd(10)


def gray_theme():
    canvas.bgcolor("dark gray")


def light_theme():
    canvas.bgcolor("white")

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

def clear():
    tim.clear()

canvas.onkeypress(key="Up", fun=move_up)
canvas.onkeypress(key="Down", fun=move_down)
canvas.onkeypress(key="Right", fun=move_right)
canvas.onkeypress(key="Left", fun=move_left)
canvas.onkeypress(key="z", fun=pen_up)
canvas.onkeypress(key="x", fun=pen_down)
canvas.onkeypress(key="c", fun=random_colors)
canvas.onkeypress(key="space", fun=clear)
canvas.onkeypress(key="g", fun=gray_theme)
canvas.onkeypress(key="e", fun=light_theme)

canvas.exitonclick()
