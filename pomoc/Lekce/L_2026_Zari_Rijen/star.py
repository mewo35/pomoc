import turtle
import math
import random

random.seed(7)

screen = turtle.Screen()
screen.setup(800, 480)
screen.bgcolor("#12001c")

t = turtle.Turtle()
t.speed(0)

def star():
    t.penup()
    for _ in range(70):
        x = random.randint(-390, 390)
        y = random.randint(-230, 230)
        t.goto(x,y)
        t.dot(random.randint(2, 4), "white")
        