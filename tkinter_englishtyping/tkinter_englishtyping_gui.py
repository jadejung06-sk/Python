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
typed_string = 'start'

def stop_text():
    add_text.pack_forget()
    global typed_string 
    typed_string = add_text.get("1.0",END)
    add_label = Label(text = 'End')
    add_label.pack()
    return typed_string

window.after(5000, stop_text) # 1 s = 1000 ms
window.after(5000, window.destroy)
window.mainloop()

##### Result
window2 = Tk()
window2.title("Result of English Words Typing Speed Tester")
window2.minsize(width=600, height=300)
window2.config(padx=30, pady=30)

wpm = cal_wpm(typed_string)
result_label = Label(text = f'Your words per minutes : {wpm}')
result_label.pack()
window2.mainloop()