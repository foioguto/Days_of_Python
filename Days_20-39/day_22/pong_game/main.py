from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()
scoreboard.update_scoreboard()
scoreboard.mid_line()

ball = Ball()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
        ball.x_move -= 2

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        ball.x_move += 2

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
