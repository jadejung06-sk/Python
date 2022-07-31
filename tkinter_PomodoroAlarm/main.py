import tkinter as tk
from urllib import response
from PIL import ImageTk, Image
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # ★
timer = None # ★
check_marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_btn_clicked():
    window.after_cancel(timer) # ★
    canvas.itemconfig(timer_text, text = f"00:00" )
    break_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0 # ★

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_btn_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    logn_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:  # 8
        count_down(logn_break_sec)
        break_label.config(text="Break", bg = YELLOW, fg = RED,  font = (FONT_NAME, 35, 'bold'))
    elif reps % 2 == 0: # 2 4 6
        count_down(short_break_sec)
        break_label.config(text="Break", bg = YELLOW, fg = PINK,  font = (FONT_NAME, 35, 'bold'))
        global check_marks
        check_marks += "✔"
        check_label.config(text = check_marks)
    else:
        count_down(work_sec) # 1 3 5 7
        break_label.config(text="Work", bg = YELLOW, fg = GREEN,  font = (FONT_NAME, 35, 'bold'))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10: # int
        # count_sec = str(count_sec).zfill(2) 
        count_sec = f"0{count_sec}" # ★ str
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}" ) # ★
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_btn_clicked()
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
start_btn = tk.Button(text= 'Start', command = start_btn_clicked, highlightthickness=0)
start_btn.grid(column= 0, row = 2)
reset_btn = tk.Button(text= 'Reset', command = reset_btn_clicked, highlightthickness=0)
reset_btn.grid(column= 2, row = 2)
### tomato timer
file = './pomodoro-start/tomato.png'
canvas = tk.Canvas(width=200, height= 224, bg = YELLOW, highlightthickness= 0) # ★
tomato_img = tk.PhotoImage(file = file)
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = f'00:00', fill = "white", font = (FONT_NAME, 35, 'bold')) # ★
canvas.grid(column=1, row=1)
### check mark
check_label = tk.Label(bg = YELLOW, fg = GREEN,  font = (FONT_NAME, 15, 'bold'))
check_label.grid(column = 1, row = 3 )
window.mainloop()
