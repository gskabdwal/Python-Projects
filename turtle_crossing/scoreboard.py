from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 250)
        self.write(arg=f"Level: {self.current_level}", move=True, align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.current_level += 1
        self.goto(-290, 250)
        self.write(arg=f"Level: {self.current_level}", move=True, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=True, align="center", font=FONT)
