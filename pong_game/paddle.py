from turtle import Turtle

WIDTH = 20/20
HEIGHT = 100/20
X_POS = 380
Y_POS = 0
MOVE = 20

class Paddle:

    def __init__(self):
        super().__init__()
        self.paddle = Turtle(shape = 'square')
        # self.paddle.hideturtle()
        self.paddle.color('white')
        self.paddle.speed('fastest')
        self.paddle.setheading(90)
        self.paddle.penup()
        self.paddle.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.paddle.goto(X_POS, Y_POS)
        # self.paddle.showturtle()

    def up(self):
        self.paddle.forward(MOVE)

    def down(self):
        self.paddle.backward(MOVE)





