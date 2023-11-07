from turtle import Screen
import time
from paddle import Paddle
from line import Line
from ball import Ball
from game_over import GameOver
from score import Score

NUMBER_OF_GAMES = 5


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

line = Line()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
double_paddle_bounce_protection = False
temp_count = 0

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.03)

    # bouncing from bottom and top wall
    if abs(ball.ycor()) > 280:
        ball.wall_bounce()

    # bouncing from paddle (additional condition with 331 to not bounce with the back of the paddle
    if abs(ball.xcor()) > 319 and (abs(ball.xcor()) < 331) and (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50):
        if not double_paddle_bounce_protection:
            ball.paddle_bounce()
            ball.increase_speed()
            double_paddle_bounce_protection = True

    # combined with if statement above protects ball from bouncing multiple times from paddle (glitch)
    if double_paddle_bounce_protection:
        temp_count += 1
        if temp_count == 10:
            temp_count = 0
            double_paddle_bounce_protection = False

    # paddle missed the ball
    if abs(ball.xcor()) > 360:
        if ball.xcor() > 0:
            r_paddle.score += 1
        else:
            l_paddle.score += 1
        ball.reset_position()
        ball.reset_speed()
        score.update_score(l_paddle.score, r_paddle.score)
        time.sleep(0.3)

    # game over
    if l_paddle.score == NUMBER_OF_GAMES or r_paddle.score == NUMBER_OF_GAMES:
        game_is_on = False
        game_over = GameOver()
        screen.update()

screen.exitonclick()
