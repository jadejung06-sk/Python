from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

##### creates the screen
screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor('black')
screen.title("My Pong Game")
screen.tracer(0) # turn off the animation

##### makes two paddles
r_paddle = Paddle((350,0))  # ★
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

##### controls the paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball_speed_tuple = (0.1, 0.05, 0.01, 0.005, 0.001)

game_is_on = True
while game_is_on:
    time.sleep(random.choice(ball_speed_tuple)) # ★★
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ##### r_paddle misses a ball    
    elif ball.xcor() > 400:
        ball.reset_position()
        scoreboard.get_score('r_paddle')
    ##### l_paddle misses a ball
    elif ball.xcor() < - 400:
        ball.reset_position()
        scoreboard.get_score('l_paddle')
    ##### detects collision with paddles       
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()    

screen.exitonclick()

##### two scoreboards

