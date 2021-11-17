from turtle import Turtle, home

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90.0
DOWN = 270.0
LEFT = 180.0
RIGHT = 0.0


class Snake(Turtle):

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


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
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        print(self.head.heading())

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        print(self.head.heading())

    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.seth(LEFT)
        print(self.head.heading())

    def right(self):
        if self.head.heading() != LEFT:
            return self.head.seth(RIGHT)
        print(self.head.heading())

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())
