from turtle import Turtle


class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)

    def draw(self):
        self.seth(270)
        self.pendown()
        while (self.ycor() > -250):
            self.pensize(3)
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
