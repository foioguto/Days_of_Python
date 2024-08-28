from turtle import Turtle
import random

COLORS = ["black", "grey", "purple", "blue", "cyan", "orange", "red", "brown"]


class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 10

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 10
