import time
from turtle import Turtle, Screen
from snake import Snake

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Python Snake Game')
my_screen.tracer(0)

new_snake = Snake()

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    new_snake.move()

my_screen.exitonclick()
