from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update()

    def update(self):
        self.write(f'LEVEL : {self.score}', align = 'left', font = FONT)

    def get_score(self):
        self.score += 1
        self.clear()
        self.update()

    def end(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align = 'center', font = FONT)
        