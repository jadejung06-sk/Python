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
r_paddle = Paddle((380,0))  # ★
l_paddle = Paddle((-380,0))
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
        ball.bounce()

        

    # if r_paddle.distance(ball) < 15:
        
        


screen.exitonclick()


##### draws a line in the middle of center
##### two scoreboards
##### needs a moving ball
##### detect when paddle misses