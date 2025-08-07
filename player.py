from turtle import Turtle

STARTING_POSITION = (0,-280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(10)

    def collision(self):
        self.goto(0,0)
        self.penup()
        self.write("GAME OVER", align="center", font=("Courier", 16, "normal"))

    def is_at_finish_line(self):
        return self.ycor() > 280

    def reset_position(self):
        self.goto(STARTING_POSITION)

