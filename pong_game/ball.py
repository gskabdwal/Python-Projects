from turtle import Turtle


class Ball(Turtle):
    ball_speed = .1

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=.6, stretch_len=.6)
        self.color("white")
        self.penup()
        self.speed(0)
        self.x = 10
        self.y = 10

    def motion(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1
  
    def bounce_x(self):
        self.x *= -1
        self.ball_speed *= .95

    def reset(self):
        self.goto(0, 0)
        self.ball_speed = .1
        self.x *= -1
