from turtle import Turtle


class Scoreboard(Turtle):
    left_score = 0
    right_score = 0

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

    def leftside(self):
        self.goto(-50, 200)
        self.write(arg=f"{self.left_score}", move=True, align="center", font=("Arial", 40, "bold"))

    def rightside(self):
        self.goto(50, 200)
        self.write(arg=f"{self.right_score}", move=True, align="center", font=("Arial", 40, "bold"))

    def updatescore(self):
        self.clear()
        self.leftside()
        self.rightside()
