from turtle import Turtle


HEIGHT = 40/20
WIDTH = 20/20

class Bars(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.create_bars()
    #     self.front_bar_list = []
    #     self.middle_bar_list = []
    #     self.end_bar_list = []


    # def create_bars(self):
    #     for front_bar in self.front_bar_list:

    #     for middle_bar in self.middle_bar_list:

    #     for end_bar in self.end_bar_list:

    def create_bars(self):
        self.color('blue')
        self.goto((-380,75))
        self.goto((-350,75))