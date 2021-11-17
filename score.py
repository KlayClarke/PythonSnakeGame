from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.color('white')
        self.speed('fastest')

    def update_score(self, score):
        self.write(f'Score: {score}', move=False, align='center', font=('Arial', 16, 'normal'))

