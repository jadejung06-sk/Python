from turtle import Turtle


WIDTH = 100/20
HEIGHT = 20/20
MOVE = 20
class Paddle(Turtle): 

    def __init__(self, position): # ★
        super().__init__()
        self.shape('square')        
        self.color('white')
        self.speed('fastest')
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.goto(position)

    def up(self):
        self.forward(MOVE)

    def down(self):
        self.backward(MOVE)

