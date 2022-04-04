from turtle import Turtle, Screen
import pandas as pd
import time

### Read csv data
IMAGE_PATH = './us-states-game-start/blank_states_img.gif'
states_data = pd.read_csv('./us-states-game-start/50_states.csv')
# print(states_data)
# state, x, y
# print(states_data.shape)

### Make a screen
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
screen.bgpic('./us-states-game-start/blank_states_img.gif')
screen.tracer(0)

### Make a game
game_is_on = True
score = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt = "Please type the name of states :").lower()
    for num in range(states_data.shape[0]):
        if answer_state == states_data.state[num].lower():
            score += 1
            screen.update()
            time.sleep(0.1)
            turtle = Turtle()
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(states_data.x[num],states_data.y[num])
            turtle.write(states_data.state[num], font = ('Arial', 8, 'normal'))

screen.exitonclick()