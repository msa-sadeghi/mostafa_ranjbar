import turtle
from time import sleep
from snake_utils import *
screen = turtle.Screen()

screen.bgcolor("black")
screen.title("snake")
screen.setup(600,600)
screen.tracer(False)

def onclose():
    global running
    running = False

root = screen._root
root.protocol("WM_DELETE_WINDOW", onclose)
root.resizable(False,False)

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)

def go_up():
    snake_head.direction = "up"
def go_down():
    snake_head.direction = "down"
def go_left():
    snake_head.direction = "left"
def go_right():
    snake_head.direction = "right"

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

running = True
while running:
    screen.update()
    if snake_head.distance(snake_food)<20:
        change_position(snake_food)

    move()
    sleep(0.2)