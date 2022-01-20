from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(3)

    def wall_bounce(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def paddle_bounce(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)

    def reset_position(self):
        self.goto(0, 0)
