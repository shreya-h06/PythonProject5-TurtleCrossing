from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.write("Level: 1", align="center", font=("Courier", 16, "normal"))

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 16, "normal"))




