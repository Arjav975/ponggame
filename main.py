# CREATE SCREEN

from turtle import Turtle, Screen
from paddle_s import Paddles
from ball_class import Ball
import time
from Scoreboard import Score

screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Separation in screen
tim = Turtle()
tim.color("white")
tim.penup()
tim.goto(0, 300)
tim.pendown()
tim.right(90)
while tim.ycor() > -300:
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()
tim.hideturtle()

# Making paddles
right_paddle = Paddles((370, 0))
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

left_paddle = Paddles((-370, 0))
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

ball = Ball()
score = Score()
game_is_on = True
while game_is_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()
    # if ball.xcor() > 370 or ball.xcor() < -370:
    #     ball.bounce_x()
    # we don't need above code
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH PADDLE
    if ball.distance(right_paddle) < 40 and ball.xcor() > 340 or ball.distance(left_paddle) < 40 and ball.xcor() < -340:
        ball.bounce_x()

    # IF RIGHT miss ball.
    if ball.xcor() > 370:
        ball.reset_position()
        score.l_points()

    # IF LEFT miss ball
    if ball.xcor() < -370:
        ball.reset_position()
        score.r_points()

screen.exitonclick()
