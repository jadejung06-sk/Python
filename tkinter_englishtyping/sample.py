YELLOW = '#FEF5AC'
BLUE = '#25316D'

from tkinter import *
import time
import random

words = ['ball', 'janitor', 'clean', 'jump', 'ride', 'laptop', 'crazy', 'help', 'say', 'dog', 'cat', 'able', 'eye', 'certain', 'hopeful', 'get', 'had', 'why', 'whole', 'child', 'face', 'little', 'shady', 'score', 'pound', 'more', 'four', 'real', 'less', 'study', 'classic', 'show', 'fight', 'their', 'interest', 'above', 'side', 'true', 'we', 'us', 'there']


window = Tk()
window.title("Typing speed tester")
window.minsize(height=400, width=600)
window.config(bg=YELLOW)


t_words = []
for _ in range(25):
    t_words.append(random.choice(words))
    t_words = list(dict.fromkeys(t_words))

final = ' '.join([str(elem) for elem in t_words])

words_label = Label(text=final, pady=50, font=("Comic Sans MS", 11, "bold"))
words_label.config(fg=BLUE, bg=YELLOW)


def check_speed(event):
    check_button.forget()
    user_entry.forget()
    words_label.forget()
    global end
    end = time.time()
    user_typed = user_entry.get()
    user_input_list = user_typed.split(" ")
    final_list = final.split(" ")

    users_time = round((end - start), 2)
    users_time_min = (users_time / 60.0)

    index = 0
    wrong_indexes = []

    for _ in range(len(final_list)):
        if user_input_list[index] == final_list[index]:
            index += 1
        else:
            wrong_indexes.append(index)
            index += 1

    wrong_words = []
    for indexx in wrong_indexes:
        wrong_words.append(final_list[indexx])
    wrong_words_for_len = len(' '.join([str(elem) for elem in wrong_words]))

    if wrong_words == []:
        perfect_label = Label(text='You got nothing wrong! Nice Job!', font=("Comic Sans MS", 11, "bold"))
        perfect_label.pack()
        perfect_label.config(fg=BLUE, bg=YELLOW)
    else:
        wrong_words_label = Label(text=f"The word(s) you got wrong were {wrong_words}.\nThese words were not counted. To get a better score, try for 100% accuracy.", font=("Comic Sans MS", 11, "bold"))
        wrong_words_label.config(fg=BLUE, bg=YELLOW)
        wrong_words_label.pack()
    global users_speed
    users_speed = round((((len(final) / 5) / users_time_min) - wrong_words_for_len), 0)
    if users_speed < 0:
        users_speed = 0
    if users_speed == 0:
        complete_failure_label = Label(text=('You really just got everthing wrong. Your speed is 0. To earn some points try to get some words right.'), font=("Comic Sans MS", 11, "bold"))
        complete_failure_label.pack()
        complete_failure_label.config(fg=BLUE, bg=YELLOW)
    speed_label = Label(text=(f"Your speed is {users_speed} WPM"), font=("Arial", 11, "bold"))
    speed_label.config(fg=BLUE, bg=YELLOW)
    speed_label.pack()






def enter_pressed(event):
    global start
    start = time.time()
    enter_button.forget()
    ready_label.forget()
    words_label.pack()
    global user_entry
    user_entry = Entry(width=95)
    user_entry.pack()
    global check_button
    check_button = Button(text='Check')
    check_button.bind("<Return>", check_speed)
    check_button.pack()




def yes_clicked():
    no.place_forget()
    yes.place_forget()
    q_label.forget()
    title_label.forget()
    is_ready.forget()
    yes.forget()
    no.forget()
    global ready_label
    ready_label = Label(text="Press Enter when you are ready to start your typing test\n\n****IMPORTANT****\nMake sure the button is highlighted. Press tab to highlight then press enter.\nDo the same before you type and when you are checking your speed.\n", font=("Comic Sans MS", 11, "bold"))
    ready_label.config(fg=BLUE, bg=YELLOW)
    ready_label.pack()
    global enter_button
    enter_button = Button(text='Enter')
    enter_button.bind("<Return>", enter_pressed)
    enter_button.pack()






def no_clicked():
    no.place_forget()
    yes.place_forget()
    q_label.forget()
    title_label.forget()
    is_ready.forget()
    yes.forget()
    no.forget()
    bye = Label(text="Ok come back when you are ready", font=("Arial", 20, "bold"))
    bye.config(fg=BLUE, bg=YELLOW)
    bye.place(y=150, x=80)





title_label = Label(text="Typing Speed Test", pady=15, font=("Comic Sans MS", 20, "italic"))
title_label.config(fg=BLUE, bg=YELLOW)
title_label.pack()

q_label = Label(text="How fast can you Type?\nLets find out!", pady=15, font=("Roboto", 15, 'italic'))
q_label.config(fg=BLUE, bg=YELLOW)
q_label.pack()

is_ready = Label(text="Are you ready to start your typing speed test?", font=("Times New Roman", 15, "bold"))
is_ready.config(fg=BLUE, bg=YELLOW)
is_ready.pack()
yes = Button(text='Yes', command=yes_clicked)
yes.place(x=200, y=200)
no = Button(text='No', command=no_clicked)
no.place(x=360, y=200)









window.mainloop()