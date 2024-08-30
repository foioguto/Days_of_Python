import turtle as t
import random

dimmy = t.Turtle()
t.colormode(255)
dimmy.speed("fastest")


def randomize_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        dimmy.color(randomize_color())
        dimmy.circle(100)
        dimmy.setheading(dimmy.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
