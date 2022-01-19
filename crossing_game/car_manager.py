from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-300,300))

    def race(self):
        self.new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(self.new_x, self.ycor())

    def difficulty(self, num):
        self.new_x = self.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * num)