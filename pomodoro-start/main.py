import tkinter as tk
from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    canvas.itemconfig(timer_text, text = count ) # ★
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=400, height = 400)
window.config(padx=100, pady=50, bg = YELLOW) # ★


### window.after()
# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# window.after(1000, say_something, 3,5,8) # ★


### label
break_label = tk.Label(text = 'Timer', bg = YELLOW, fg = PINK,  font = (FONT_NAME, 35, 'bold'))
break_label.grid(column = 1, row = 0 )

## buttons
def start_btn_clicked():
    print("start_btn")
    count_down(5)
start_btn = tk.Button(text= 'Start', command = start_btn_clicked, highlightthickness=0)
start_btn.grid(column= 0, row = 2)

def start_btn_clicked():
    print("start_btn")
reset_btn = tk.Button(text= 'Reset', command = start_btn_clicked, highlightthickness=0)
reset_btn.grid(column= 2, row = 2)

### tomato timer
file = './pomodoro-start/tomato.png'
canvas = tk.Canvas(width=200, height= 224, bg = YELLOW, highlightthickness= 0) # ★
tomato_img = tk.PhotoImage(file = file)
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = f'00:00', fill = "white", font = (FONT_NAME, 35, 'bold')) # ★
canvas.grid(column=1, row=1)

### check mark
check_marks = "✔"
check_label = tk.Label(text = check_marks, bg = YELLOW, fg = GREEN,  font = (FONT_NAME, 15, 'bold'))
check_label.grid(column = 1, row = 3 )

count_down(5)

window.mainloop()
