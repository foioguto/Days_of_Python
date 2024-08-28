from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.refresh()
        self.setheading(90)

    def walk(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def refresh(self):
        self.goto(x=0, y=-280)
