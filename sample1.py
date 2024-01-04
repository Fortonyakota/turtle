import turtle
from random import random, uniform
import math

screen = turtle.Screen()
screen.bgcolor('black')
t = turtle.Turtle()
t.shape()
t.speed(10000)

def draw_star(radius):
    while True:
        random_radius = uniform(0, radius)
        random_angle = uniform(0, 360)
        x = random_radius * math.cos(math.radians(random_angle))
        y = random_radius * math.sin(math.radians(random_angle))

        t.goto(x, y)
        t.pencolor(random(), random(), random())

draw_star(50)

screen.exitonclick()
