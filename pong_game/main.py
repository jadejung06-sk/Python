from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

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

##### controls the paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1) # ★
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ##### r_paddle misses a ball    
    elif ball.xcor() > 400:
        ball.reset_position()
    ##### l_paddle misses a ball
    elif ball.xcor() < - 400:
        ball.reset_position()
    ##### detects collision with paddles       
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()    

screen.exitonclick()

##### two scoreboards

