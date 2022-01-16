from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width = 600, height = 600) # ★
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0) # ★

snake = Snake()
food = Food()
scoreboard = Scoreboard()

##### control the direction
screen.listen() 
screen.onkey(snake.up,"Up") # ★
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

##### make a wall

game_is_on = True
while game_is_on:
    screen.update() # ★
    time.sleep(0.1)
    snake.move()

    ##### detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.get_score()
    ##### detect collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 :
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
    ##### Detect collision with tail.
    for tail in snake.segments[1:]:
        if snake.head.distance(tail) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick() # ★