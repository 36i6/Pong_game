from turtle import Turtle

START_RIGHT_PADDLE_POS = (620, 0)
START_LEFT_PADDLE_POS = (-620, 0)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5)

    def start_right_paddle(self):
        self.setposition(x=START_RIGHT_PADDLE_POS[0], y=START_RIGHT_PADDLE_POS[1])
        self.showturtle()

    def start_left_paddle(self):
        self.setposition(x=START_LEFT_PADDLE_POS[0], y=START_LEFT_PADDLE_POS[1])
        self.showturtle()

    def move_up(self):
        self.forward(30)

    def move_down(self):
        self.back(30)
