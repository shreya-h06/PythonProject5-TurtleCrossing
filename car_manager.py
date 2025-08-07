from turtle import Turtle
import random

COLORS = [
    "red", "orange", "yellow", "green", "blue",
    "purple", "pink", "brown", "cyan", "magenta",
    "lime", "turquoise", "gold", "violet", "salmon"
]


class Car(Turtle):
    car_speed = 5
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(300, random.randint(-250, 250))


    def move(self):
        self.forward(Car.car_speed)

    @classmethod
    def increase_speed(cls):
        cls.car_speed += 1
