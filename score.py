from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 30, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 250)
        self.update_score(0, 0)

    def update_score(self, r_score, l_score):
        self.clear()
        self.write(f"{r_score}   {l_score}", align=ALIGNMENT, font=FONT)
