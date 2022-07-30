from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(stretch_wid=.5,stretch_len=.5)
        self.refresh()


    def refresh(self):
        new_x = random.randint(-280,280)
        new_y = random.randint(-230, 230)
        self.goto(new_x,new_y)

