from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

bobby = Turtle()
bobby.shape('turtle')
# bobby.fillcolor("green")
bobby.color("dark green")
bobby.pensize(4)
scr = Screen()

def forward():
    bobby.forward(15)

def back():
    bobby.backward(15)

def left():
    bobby.left(90)

def right():
    bobby.right(90)


def draw_square(side):
    for i in range(4):
        bobby.forward(side)
        bobby.right(90)


def draw_triangle(side):
    for i in range(3):
        bobby.forward(side)
        bobby.left(120)


def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


scr.listen()


# bobby.pencolor(get_color())
# draw_square(200)
bobby.pencolor(get_color())
# draw_triangle(200)
bobby.circle(150)
# scr.onkey(forward, 'f')
# scr.onkey(back, 'd')
# scr.onkey(left, 'j')
# scr.onkey(right, 'k')

scr.exitonclick()