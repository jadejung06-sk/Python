import tkinter
THEME_COLOR = "#375362"
"""
Ref. 1 Python tkinter class
https://076923.github.io/posts/Python-tkinter-15/
"""
# window 4(3) x 2(1) or 3 x 2 : quizzler
window = tkinter.Tk()
window.title(string = "quizzler")
window.geometry("390x500")
# score_label
score = 0
score_label = tkinter.Label(window, text=f"score : {score}")
# quiz canvas
canvas = tkinter.Canvas(window, relief='solid', bd = 2)
canvas.create_text(110, 80, text = "quiz")
# v check box in the left side
def ok_status():
    print("ok")
v_button = tkinter.Button(window, command = ok_status)
# x check box on the right side
x_button = tkinter.Button(window, command= ok_status)
# grid some items
score_label.grid(row= 0,column=1)
canvas.grid(row=1, column=0, columnspan=2)
v_button.grid(row=3, column=0)
x_button.grid(row=3, column=1)

window.mainloop()
