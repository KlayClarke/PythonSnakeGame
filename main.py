from turtle import Turtle, Screen

snake = Turtle('square')
snake.color('white')

snake_2 = Turtle('square')
snake_2.setpos(x=-20, y=0)
snake_2.color('white')

snake_3 = Turtle('square')
snake_3.setpos(x=-40, y=0)
snake_3.color('white')












my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Python Snake Game')













my_screen.exitonclick()