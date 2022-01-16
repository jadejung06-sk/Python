from re import L
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.update_score()

    def update_score(self):
        self.write(f"Score :  {self.score}", move = False, align= ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move = False, align= ALIGNMENT, font = FONT)

    def get_score(self):
        self.score += 1
        self.clear() # ★
        self.update_score()

