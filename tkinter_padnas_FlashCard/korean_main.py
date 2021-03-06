import tkinter as tkt
import pandas as pd
import random

def next_card():
    canvas.itemconfig(card_image, image = CARD_FRONT)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "English", fill = "black") # ★
    canvas.itemconfig(card_word, text = current_card["English"], fill="black")
    flip_timer = window.after(3000, func = flip_card)

def remove_card():
    global data
    index_names = data[data.English == current_card["English"]].index
    data.drop(index_names, inplace= True)
    data.to_csv("./flash-card-project-start/data/words_to_learn_Korean.csv", index= False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text = "Korean", fill = 'black') # ★
    canvas.itemconfig(card_word, text = current_card["Korean"], fill= 'black')
    canvas.itemconfig(card_image, image = CARD_BACK)

BACKGROUND_COLOR = "#B1DDC6"
window = tkt.Tk()
window.title("Flashy")
window.minsize(width=1000, height=800)
window.config(padx=50, pady= 50, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_card)

WIDTH = 800
HEIGHT = 526
CARD_BACK = tkt.PhotoImage(file = "./flash-card-project-start/images/card_back.png") # ★
CARD_FRONT = tkt.PhotoImage(file = "./flash-card-project-start/images/card_front.png")
CORRECT = tkt.PhotoImage(file = "./flash-card-project-start/images/right.png")
WRONG = tkt.PhotoImage(file = "./flash-card-project-start/images/wrong.png")

try:
    data =  pd.read_csv("./flash-card-project-start/data/words_to_learn_Korean.csv")
except FileNotFoundError:
    data =  pd.read_csv("./flash-card-project-start/data/Korean_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}
# print("1", to_learn)
canvas = tkt.Canvas(window, width = WIDTH, height= HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0) # ★
card_image = canvas.create_image(WIDTH/2,HEIGHT/2, image = CARD_FRONT)
# canvas.create_image(550,720, image = CORRECT)
# canvas.create_image(250,720, image = WRONG)

### labels
## words method 1
# num = random.randint(0,WORDS.shape[0])
# french_word = WORDS.French
# canvas.create_text(400,150, text = f'{french_word.name}', font=("Ariel", 40, "italic"))
# canvas.create_text(400,260, text = f'{french_word[num]}', font=("Ariel", 60, "bold"))

## words method 2
### btns
correct_btn = tkt.Button(window, image = CORRECT, command=remove_card)
wrong_btn = tkt.Button(window, image = WRONG, command=next_card)
# french_wd = random_word()
card_title = canvas.create_text(400,150, text = f'', font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,260, text = f'', font=("Ariel", 60, "bold"))

### grid
canvas.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row= 1, column = 0)
correct_btn.grid(row = 1, column = 1)

### action
next_card()

window.mainloop()
