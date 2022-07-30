from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.screensize(600, 500)

screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(fun=snake.up,key= "Up")
screen.onkey(fun=snake.down,key= "Down")
screen.onkey(fun=snake.left,key= "Left")
screen.onkey(fun=snake.right,key= "Right")

game_is_on = True

while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move()
        food
        scoreboard
        if snake.turtles[0].distance(food) < 15:
                snake.total_seg += 1
                snake.add_seg()
                food.refresh()
                scoreboard.score += 1
                scoreboard.inc_scoreboard(score=scoreboard.score)

        if snake.turtles[0].xcor() > 300 or snake.turtles[0].ycor() > 230 or snake.turtles[0].xcor() < -300 or snake.turtles[0].ycor()< -250:
                game_is_on = False
                scoreboard.game_over()


        for seg in snake.turtles[1:]:


               if snake.turtles[0].distance(seg) < 10:
                       game_is_on = False
                       scoreboard.game_over()





screen.exitonclick()
