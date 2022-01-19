import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen() # ★
screen.onkey(player.move, 'Up')

car_list = []
i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() % 50:
        for _ in range(1):
            car_manager = CarManager()
            car_manager.difficulty(i)
            i += 1
            car_list.append(car_manager)
            for car in car_list:
                car.race()
                if player.distance(car) < 10:
                    game_is_on = False
                    scoreboard.end()
    if player.finish():
       scoreboard.get_score()
       player.start()
    
screen.exitonclick()