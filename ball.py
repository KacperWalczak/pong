from turtle import Turtle
from random import randint, choice
MOVING_DISTANCE = 10
SPEEDING_UP = 5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.move_distance = MOVING_DISTANCE
        self.penup()
        self.shape('circle')
        # self.setheading(randint(0, 360))
        self.set_the_heading()

    def set_the_heading(self):
        self.setheading(choice(list(set(range(0, 360)) - set(range(70, 110)) - set(
            range(250, 290)) - set(range(0, 10)) - set(range(350, 360)) - set(range(170, 190)))))

    def move(self):
        self.forward(self.move_distance)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(180 - self.heading())

    def reset_position(self):
        self.goto(0, 0)
        self.set_the_heading()

    def increase_speed(self):
        self.move_distance += SPEEDING_UP

    def reset_speed(self):
        self.move_distance = MOVING_DISTANCE






