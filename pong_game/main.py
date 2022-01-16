from turtle import Turtle, Screen
from paddle import Paddle

##### create the screen
screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor('black')
screen.title("My Pong Game")
screen.tracer(0) # turn off the animation

paddle = Paddle()
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

WIDTH = 20/20
HEIGHT = 100/20
X_POS = 380
Y_POS = 0
MOVE = 20

# paddle = Turtle(shape = 'square')
# paddle.color('white')
# paddle.speed('fastest')
# paddle.setheading(90)
# paddle.penup()
# paddle.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
# paddle.goto(X_POS, Y_POS)

game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()

##### makes two bar with 4 blocks
##### draws a line in the middle of center
##### two scoreboards
##### needs a moving ball
##### detect when paddle misses