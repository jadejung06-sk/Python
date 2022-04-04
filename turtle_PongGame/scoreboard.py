from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
 
    def update_score(self):
        self.goto(-100, 200)
        self.write(f'{self.l_score}', align= 'center', font = ('Courier', 80, 'normal'))
        self.goto(100,200)
        self.write(f'{self.r_score}', align= 'center', font = ('Courier', 80, 'normal'))
        

    def get_score(self, score):
        if score == 'r_paddle':
            self.l_score += 1
            self.clear()
            self.update_score()
        else:
            self.r_score += 1
            self.clear()
            self.update_score()