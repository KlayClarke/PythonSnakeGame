from turtle import Turtle

alignment = 'center'
font = ('Arial', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.score = 0
        self.high_score = 0

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}' f'  High Score: {self.high_score}', move=False, align=alignment, font=font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
