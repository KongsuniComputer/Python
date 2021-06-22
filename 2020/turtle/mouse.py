import turtle
import random

def draw(x, y):
    turtle.penup()
    turtle.goto(x, y)
    r = random.randint(1, 100)
    turtle.pendown()
    turtle.circle(r)

turtle.pensize(10)
turtle.onscreenclick(draw)
turtle.listen()
turtle.mainloop()
