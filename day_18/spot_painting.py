"""
import colorgram

rgb_colors = []
colors = colorgram.extract('art.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors) """
import turtle as t
import random

dimmy = t.Turtle()
screen = t.Screen()

t.colormode(255)
numbers_of_dots = 100

color_list = [(227, 226, 225), (235, 236, 238), (231, 235, 232), (180, 66, 36), (212, 150, 97), (15, 25, 42),
              (239, 209, 93),
              (234, 63, 34), (153, 27, 20), (72, 30, 33), (84, 92, 114), (67, 42, 36), (118, 33, 38), (160, 141, 71),
              (137, 153, 164),
              (177, 90, 99), (50, 52, 126), (157, 66, 71), (234, 169, 158), (168, 143, 149), (98, 115, 114),
              (15, 27, 27),
              (157, 165, 164), (220, 174, 179), (189, 189, 197), (75, 70, 46), (121, 122, 144), (187, 194, 189),
              (118, 132, 135)]


dimmy.speed("fastest")
dimmy.penup()
dimmy.hideturtle()

dimmy.setheading(225)
dimmy.forward(300)
dimmy.setheading(0)

for count in range(1, numbers_of_dots + 1):
    dimmy.dot(20, random.choice(color_list))
    dimmy.forward(50)

    if count % 10 == 0:
        dimmy.setheading(90)
        dimmy.forward(50)
        dimmy.setheading(180)
        dimmy.forward(500)
        dimmy.setheading(0)

screen.exitonclick()
