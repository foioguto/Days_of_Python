import turtle as tt
import random

dimmy = tt.Turtle()
dimmy.pensize(15)
dimmy.speed(3)
tt.colormode(255)


def randomize_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(200):
    dimmy.color(randomize_color())
    choice = random.randint(1, 4)
    if choice == 1:
        dimmy.forward(30)
    elif choice == 2:
        dimmy.back(30)
    elif choice == 3:
        dimmy.left(90)
        dimmy.forward(30)
    else:
        dimmy.right(90)
        dimmy.forward(30)
# setheading(direction angle) = better solution
