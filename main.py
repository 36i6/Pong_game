from turtle import Screen

import score
from paddles import Paddle
from ball import Ball
from score import Score

SCREEN_RESOLUTION = (1280, 960)

screen = Screen()
screen.setup(width=SCREEN_RESOLUTION[0], height=SCREEN_RESOLUTION[1])
screen.title("Pong")
screen.bgcolor("black")
screen.listen()

game_is_over = 3
right_paddle = Paddle()
left_paddle = Paddle()

user_1_score = Score()
user_1_score.goto(score.LEFT_SCORE_CORD)
user_1_score.update_score()
user_2_score = Score()
user_2_score.goto(score.RIGHT_SCORE_CORD)
user_2_score.update_score()
right_paddle.start_right_paddle()
left_paddle.start_left_paddle()

screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
ball = Ball()

while game_is_over != 0:

    if ball.xcor() < -(SCREEN_RESOLUTION[0] / 2 - 10):
        user_2_score.score += 1
        user_2_score.update_score()
        game_is_over -= 1
        ball.reset_position()
        pass
    if ball.xcor() > (SCREEN_RESOLUTION[0] / 2 - 10):
        user_1_score.score += 1
        user_1_score.update_score()
        game_is_over -= 1
        ball.reset_position()
        pass
    if abs(ball.ycor()) > (SCREEN_RESOLUTION[1] / 2 - 10):
        ball.wall_bounce()
    if (ball.distance(right_paddle) < 20 or ball.distance(left_paddle) < 20) or \
            ((ball.distance(right_paddle) < 51 or ball.distance(left_paddle) < 51) and
             (abs(ball.xcor()) > 599)):
        ball.paddle_bounce()
        while ball.distance(right_paddle) < 45 or ball.distance(left_paddle) < 45:
            ball.move()

    ball.move()

screen.exitonclick()
