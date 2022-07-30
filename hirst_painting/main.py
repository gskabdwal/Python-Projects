import turtle
from turtle import Turtle, Screen
import random
# import colorgram


# colors = colorgram.extract("image.jpg",50)
# col = []
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#
#     col_tuple = (r,g,b)
#     col.append(col_tuple)
#
# print(col)

color_list = [(143, 162, 184), (205, 137, 168), (197, 174, 8), (149, 15, 31), (67, 24, 31), (11, 143, 55), (214, 158, 101), (239, 212, 61), (122, 71, 101), (53, 28, 25), (205, 62, 24), (2, 109, 61), (226, 170, 199), (246, 214, 2), (26, 178, 88), (240, 79, 29), (16, 172, 190), (116, 188, 146), (187, 92, 116), (187, 182, 212), (36, 35, 42), (149, 13, 10), (155, 208, 218), (4, 106, 111), (231, 171, 161), (115, 121, 159), (160, 209, 181), (4, 75, 25), (35, 60, 117), (119, 126, 0)]

tim = Turtle()
screen = Screen()
tim.shape("turtle")
screen.colormode(255)


tim.penup()
tim.goto(-200,-200)


tim.hideturtle()
for y in range(10):
    for x in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)


    tim.goto(-200, tim.ycor() + 50)






screen.exitonclick()