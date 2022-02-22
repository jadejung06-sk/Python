import tkinter as tkt
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
window = tkt.Tk()
window.title("Flashy")
window.minsize(width=1000, height=800)
window.config(padx=50, pady= 50, bg = BACKGROUND_COLOR)
WIDTH = 800
HEIGHT = 526
CARD_BACK = tkt.PhotoImage(file = "./flash-card-project-start/images/card_back.png") # ★
CARD_FRONT = tkt.PhotoImage(file = "./flash-card-project-start/images/card_front.png")
CORRECT = tkt.PhotoImage(file = "./flash-card-project-start/images/right.png")
WRONG = tkt.PhotoImage(file = "./flash-card-project-start/images/wrong.png")
WORDS =  pd.read_csv("./flash-card-project-start/data/french_words.csv")
canvas = tkt.Canvas(window, width = WIDTH, height= HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0) # ★
canvas.create_image(WIDTH/2,HEIGHT/2, image = CARD_FRONT)
canvas.create_text(400,150, text = f'Title', font=("Ariel", 40, "italic"))
canvas.create_text(400,260, text = f'word', font=("Ariel", 60, "bold"))
# canvas.create_image(550,720, image = CORRECT)
# canvas.create_image(250,720, image = WRONG)

### labels
title_label = tkt.Label(canvas, text = f"title")

### btns
correct_btn = tkt.Button(window, image = CORRECT)
wrong_btn = tkt.Button(window, image = WRONG)

### grid
canvas.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row= 1, column = 0)
correct_btn.grid(row = 1, column = 1)

print(WORDS)
window.mainloop()