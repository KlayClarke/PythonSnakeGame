from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.snake.append(new_segment)

    def move(self):

        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x_cord = self.snake[seg_num - 1].xcor()
            new_y_cord = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=new_x_cord, y=new_y_cord)
        self.snake[0].forward(move_distance)

    def up(self):
        self.snake[0].seth(90)

    def down(self):
        self.snake[0].seth(270)

    def left(self):
        self.snake[0].seth(180)

    def right(self):
        self.snake[0].seth(0)

