from turtle import Turtle
PADDLE_MOVING_STEP = 25


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.shape('square')
        self.goto(cor[0], cor[1])
        self.shapesize(5, 1)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)

