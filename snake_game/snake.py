from turtle import Turtle


class Snake:
    total_seg = 3

    def __init__(self):

        self.turtles = []
        self.align = 0
        for x in range(self.total_seg):
             self.add_seg()


    def add_seg(self):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        if self.total_seg == 3:
            tim.goto(0 + self.align, 0)
        if self.total_seg > 3:
            tim.goto(self.turtles[-1].position())
        self.align -= 20
        self.turtles.append(tim)


    def move(self):

        for seg_no in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_no - 1].xcor()
            new_y = self.turtles[seg_no - 1].ycor()
            self.turtles[seg_no].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].seth(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].seth(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].seth(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].seth(0)
