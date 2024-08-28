from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Cross Game")
screen.tracer(0)

cars = Cars()

scoreboard = Scoreboard()

player = Player()
player.walk()

screen.listen()

screen.onkeypress(player.walk, "w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_line():
        player.refresh()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()
