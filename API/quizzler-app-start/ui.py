import tkinter
# from main import quiz
# from data import question_data
THEME_COLOR = "#375362"
class QuizInterface:
    """
    Ref. 1 Python tkinter class
    https://076923.github.io/posts/Python-tkinter-15/
    """

    def __init__(self):
        self.window = tkinter.Tk()   
    # window 4(3) x 2(1) or 3 x 2 : quizzler
        self.window.title(string = "quizzler")
        # self.window.geometry("500x500")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

    # images
        self.x_img = tkinter.PhotoImage(file = "./API/quizzler-app-start/images/false.png")
        self.v_img = tkinter.PhotoImage(file = "./API/quizzler-app-start/images/true.png")

    # score_label
        self.score = 0
        self.score_label = tkinter.Label(self.window, text=f"score : {self.score}", fg = 'white', bg = THEME_COLOR)
    # quiz canvas
        self.canvas = tkinter.Canvas(self.window, height=250, width=300)
        self.text = self.canvas.create_text(150, 125, text = "quiz", font=('Arial', 20, "italic"), fill = THEME_COLOR)

        def ok_status():
            # question = quiz_brain.next_question()
            self.canvas.itemconfig(self.text, text = f"change" )
            print("ok")

        # v check box in the left side
        self.v_button = tkinter.Button(self.window, command = ok_status, image= self.v_img)
        # x check box on the right side
        self.x_button = tkinter.Button(self.window, command= ok_status, image = self.x_img)

    # grid some items
        self.score_label.grid(row= 0,column=1, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.v_button.grid(row=2, column=0, pady=20)
        self.x_button.grid(row=2, column=1, pady=20)

        self.window.mainloop()
