from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time
import random



all_cars = []

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player  = Player()
score = Scoreboard()


screen.listen()
screen.onkey(player.move_up,"Up")

car_spawn_chance = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, car_spawn_chance) == 1:
        car = Car()
        all_cars.append(car)

    for car in all_cars:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
            player.collision()

    if player.is_at_finish_line():
        player.reset_position()
        score.increase_level()
        Car.increase_speed()
        if car_spawn_chance > 2:
            car_spawn_chance -= 1

screen.exitonclick()