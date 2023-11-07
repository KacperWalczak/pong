from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)
