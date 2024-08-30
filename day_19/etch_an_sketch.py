import turtle as t

dimmy = t.Turtle()
screen = t.Screen()


def forward():
    dimmy.forward(10)


def back():
    dimmy.back(10)


def left():
    new_heading = dimmy.heading() + 10
    dimmy.setheading(new_heading)


def right():
    new_heading = dimmy.heading() - 10
    dimmy.setheading(new_heading)


def clear():
    dimmy.clear()
    dimmy.penup()
    dimmy.home()
    dimmy.setheading(90)
    dimmy.pendown()


dimmy.setheading(90)
dimmy.shape("turtle")
dimmy.shapesize(3)
dimmy.fillcolor("green")
dimmy.pencolor("brown")
dimmy.pensize("6")

screen.listen()
screen.onkeypress(forward, "w")
screen.onkeypress(back, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(clear, "c")

screen.exitonclick()
