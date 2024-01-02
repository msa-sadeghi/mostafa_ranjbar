import turtle
import random
def create_turtle(shape, color):
    my_turtle = turtle.Turtle()
    my_turtle.shape(shape)
    my_turtle.color(color)
    my_turtle.penup()
    return my_turtle

def change_position(object):
    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    object.goto(x,y)
