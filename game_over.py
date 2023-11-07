from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 50)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
