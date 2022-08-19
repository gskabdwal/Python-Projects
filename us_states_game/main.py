import turtle

import pandas as pandas

screen = turtle.Screen()
screen.title("US States game")
screen.addshape("blank_states_img.gif")

tim = turtle.Turtle()
jerry = turtle.Turtle()
jerry.penup()
jerry.hideturtle()

tim.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()
correct_guesses = 0
while correct_guesses < 50:

    answer = screen.textinput(
        f"Guess the name ", f"What is another States name (Correct guesses: {correct_guesses}/50) : ").title()
    if answer == "Exit":
        break
    if answer in states_list[1::]:
        jerry.goto(int(data[data["state"] == answer]["x"]),
                   int(data[data["state"] == answer]["y"]))
        jerry.write(arg=answer, move=True, align="center",
                    font=("Arial", 8, "normal"))
        correct_guesses += 1
        states_list.remove(answer)

pandas.DataFrame(states_list).to_csv("left_states.txt")
