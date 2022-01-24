from turtle import Turtle, Screen
import pandas as pd
import time

IMAGE_PATH = './us-states-game-start/blank_states_img.gif'
### Make a screen
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
screen.bgpic('./us-states-game-start/blank_states_img.gif')

### Read csv data
data = pd.read_csv('./us-states-game-start/50_states.csv')
all_states = data.state.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    score = len(guessed_states)
    answer_state = screen.textinput(title=f"{score}/50 States Correct", 
    prompt = "Please type the name of states :").title() # ★

    if answer_state == 'Exit':
        for correct_state in all_states:
            if correct_state in guessed_states:
                pass
            else:
                missed_states.append(correct_state)
        new_data = pd.DataFrame( {'state' : missed_states})
        new_data.to_csv("./us-states-game-start/states_to_learn.csv", header = None)
    if answer_state in all_states: # ★
        guessed_states.append(answer_state)        
        t = Turtle()
        t.hideturtle()
        t.penup()
        print(answer_state)
        state_data = data[data.state == answer_state] # ★
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    
# new_data = pd.DataFrame( {'States' : missed_states})
# print(new_data)


