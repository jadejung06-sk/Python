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

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=400, height = 400)
window.config(padx=100, pady=50)

### label
break_label = tk.Label(text = 'Break', fg = PINK, font=20)
break_label.grid(column = 1, row = 0 )

## buttons
def start_btn_clicked():
    print("start_btn")
start_btn = tk.Button(text= 'Start', command = start_btn_clicked)
start_btn.grid(column= 0, row = 2)

def start_btn_clicked():
    print("start_btn")
reset_btn = tk.Button(text= 'Reset', command = start_btn_clicked)
reset_btn.grid(column= 2, row = 2)

### tomato timer
file = './pomodoro-start/tomato.png'
img = ImageTk.PhotoImage(Image.open(file))
panel = tk.Label(window, image= img).grid(column=1, row=1) # ★
panel = tk.Label(text="test", fg='black', font = 200).grid(column=1, row=1) 





window.mainloop()
