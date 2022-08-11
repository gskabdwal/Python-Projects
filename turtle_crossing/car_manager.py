from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():

    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_cars(self):
        chance = random.randint(0, 5)
        if chance == 0:
            car = Turtle()
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.shapesize(stretch_wid=.875, stretch_len=1.75)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-230, 250))
            self.cars.append(car)

    def traffic_move(self):
        for car in self.cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def speed_increase(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
