import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
traffic = CarManager()
screen.listen()

screen.onkey(key="Up", fun=player.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    traffic.create_cars()
    traffic.traffic_move()

    for car in traffic.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 300:
        player.level_up()
        scoreboard.update_score()
        traffic.speed_increase()

screen.exitonclick()
