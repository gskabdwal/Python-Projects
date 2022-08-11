from turtle import Screen
from divider import Divider
from scoreboard import Scoreboard
from ball import Ball
from players import Players
import time

screen = Screen()

screen.screensize(canvwidth=700, canvheight=500)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

divider = Divider()

divider.draw()

scoreboard = Scoreboard()
scoreboard.leftside()
scoreboard.rightside()

playerleft = Players()
playerright = Players()

playerleft.goleft()
playerright.goright()

screen.listen()

screen.onkey(fun=playerleft.up, key="w")
screen.onkey(fun=playerleft.down, key="s")

screen.onkey(fun=playerright.up, key="Up")
screen.onkey(fun=playerright.down, key="Down")

ball = Ball()

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.motion()

    if ball.xcor() > 390:
        ball.reset()
        scoreboard.left_score += 1
        scoreboard.updatescore()
        if scoreboard.left_score >= 5:
            game_on = False

    if ball.xcor() < -390:
        ball.reset()
        scoreboard.right_score += 1
        scoreboard.updatescore()
        if scoreboard.right_score >= 5:
            game_on = False

    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()

    if (playerright.distance(ball) < 50 and ball.xcor() > 360) or (
            playerleft.distance(ball) < 50 and ball.xcor() < -360):
        ball.bounce_x()

screen.exitonclick()
