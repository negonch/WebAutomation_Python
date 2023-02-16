from turtle import Turtle, Screen, colormode
from random import randint, randrange

colormode(255)

bobby = Turtle()
bobby.speed(30)
bobby.shape('turtle')
bobby.color("dark green")
bobby.pensize(4)
bobby.left(90)

scr = Screen()

def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_flower(petals=None, petal_radias=None):
    if not petals:
        petals = randint(3, 12)
    stem_length = randrange(160, 210, 10)
    bobby.forward(stem_length)
    if not petal_radias:
        petal_radias = randrange(10, 30, 5)
    # bobby.pencolor(get_color())
    for p in range(petals):
        bobby.pencolor(get_color())
        bobby.circle(petal_radias)
        bobby.left(360/petals)
    bobby.up()
    bobby.backward(stem_length)
    bobby.down()
    bobby.pencolor("dark green")

def draw_field():
    for i in range(5):
        draw_flower()
        bobby.left(90)
        bobby.up()
        bobby.forward(130)
        bobby.down()
        bobby.right(90)

scr.listen()

bobby.penup()
bobby.goto(250, -200)
bobby.pendown()

# draw_flower()
draw_field()

scr.exitonclick()
