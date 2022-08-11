from turtle import Turtle


class Players(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(.5, 2.5)
        self.seth(90)

    def goleft(self):
        self.goto(-380, 0)

    def goright(self):
        self.goto(380, 0)

    def up(self):
        if self.ycor() < 230:
            self.forward(30)

    def down(self):
        if self.ycor() > -230:
            self.backward(30)
