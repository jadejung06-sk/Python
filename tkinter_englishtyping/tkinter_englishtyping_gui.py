from englishtyping import cal_wpm, test_string
from tkinter import *

window = Tk()
window.title("English Words Typing Speed Tester")
window.minsize(width=600, height=300)
window.config(padx=30, pady=30)

prb_label = Label(text = 'Type words below this table.', font = ("Courier", 20, "bold"))
prb_label.pack()
prb_text = Text( window, height = 10, wrap='word')
prb_text.insert(INSERT, test_string)

prb_text.configure(font=("Courier", 12, "italic"))
prb_text.pack()
add_text = Text()
add_text.pack()

## method 1 : Label
# typed_string = StringVar()
# hid_label = Label(textvariable=typed_string)
## method 2 : Text
hid_text = Text()


def stop_text():
    add_text.pack_forget()
    # typed_string.set(add_text.get("1.0",END))
    add_label = Label(text = 'End')
    add_label.pack()

# def get_text():
    # add_text.get("1.0",END)

# add_text.after(5000, get_text)    
# word = add_text.get("1.0",END)
window.after(5000, stop_text) # 1 s = 1000 ms
hid_text.pack()

# print(typed_string)
# print(word)
# print(add_text)

window.mainloop()


# import tkinter as tk
# import datetime

# def timer():
#     print(datetime.datetime.now())
#     app.after(1000, timer)

# app = tk.Tk()
# app.title('Timer')

# app.after(1, timer)

# exit_button = tk.Button(app, text="Exit", fg="red", command=app.destroy)
# exit_button.pack()

# app.mainloop()