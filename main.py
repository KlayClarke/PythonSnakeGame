import time
from turtle import Turtle, Screen

squares = ['square_1', 'square_2', 'square_3']
snake = []
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Python Snake Game')
my_screen.tracer(0)

starting_positions = 0

for square in squares:
    square = Turtle('square')
    square.setpos(x=starting_positions, y=0)
    starting_positions -= 20
    square.color('white')
    square.penup()
    snake.append(square)

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x_cord = snake[seg_num - 1].xcor()
        new_y_cord = snake[seg_num - 1].ycor()
        snake[seg_num].goto(x=new_x_cord, y=new_y_cord)
    snake[0].forward(20)

# while game_is_on:
#     for square in squares:


my_screen.exitonclick()
