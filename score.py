from turtle import Turtle

LEFT_SCORE_CORD = (-580, 400)
RIGHT_SCORE_CORD = (540, 400)
FONT = ("Console", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "left", font=FONT)
