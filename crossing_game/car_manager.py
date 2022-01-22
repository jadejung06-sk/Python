from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.all_cars = [] # ★

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1: # ★
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
<<<<<<< HEAD
            self.all_cars.append(new_car) # ★
    
    def increased_speed(self, level): 
        self.speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level) # ★
=======
            self.all_cars.append(new_car)
>>>>>>> parent of c118090 (all done)

    def race(self):
        for car in self.all_cars:
            self.new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(self.new_x, car.ycor())

    def difficulty(self, level):
        self.new_x = self.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level)