from turtle import Turtle, Screen


snakes = ['snake_1', 'snake_2', 'snake_3']


def create_snake():
    starting_positions = 0
    for snake in snakes:
        snake = Turtle('square')
        snake.setpos(x=starting_positions, y=0)
        starting_positions -= 20
        snake.color('white')

create_snake()


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Python Snake Game')

my_screen.exitonclick()
