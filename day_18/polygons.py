import turtle as tt
import random

dimmy = tt.Turtle()

colours = ["red", "blue", "green", "yellow", "purple", "cyan", "brown"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        dimmy.forward(100)
        dimmy.right(angle)


for shape_side_n in range(3, 11):
    dimmy.color(random.choice(colours))
    draw_shape(shape_side_n)
