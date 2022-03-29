import tkinter
from quiz_brain import QuizBrain

# from main import quiz
# from data import question_data
THEME_COLOR = "#375362"
class QuizInterface:
    """
    Ref. 1 Python tkinter class
    https://076923.github.io/posts/Python-tkinter-15/
    """

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
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
        self.score_label = tkinter.Label(self.window, text=f"score : {self.score}", fg = 'white', bg = THEME_COLOR, font = ('Arial', 12, "bold"))
    # quiz canvas
        self.canvas = tkinter.Canvas(self.window, height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width = 280, text = "quiz", font=('Arial', 20, "italic"), fill = THEME_COLOR)

        def True_btn():
            q_text = self.quiz.next_question()
            self.user_answer = "True"
            self.quiz.check_answer(self.user_answer)  
            self.canvas.itemconfig(self.question_text, text = q_text)
            # self.canvas.itemconfig(self.window, fill = 'green')
            self.score_label.config(text=f"score : {self.quiz.score}", font = ('Arial', 12, "bold"))
            # print("ok")

        def False_btn():
            q_text = self.quiz.next_question()
            self.user_answer = "False"
            self.quiz.check_answer(self.user_answer)  
            self.canvas.itemconfig(self.question_text, text = q_text)
            self.score_label.config(text=f"score : {self.quiz.score}", font = ('Arial', 12, "bold"))
            # print("False")

        # v check box in the left side
        self.v_button = tkinter.Button(self.window, command = True_btn, image= self.v_img)
        # x check box on the right side
        self.x_button = tkinter.Button(self.window, command= False_btn, image = self.x_img)

    # grid some items
        self.score_label.grid(row= 0,column=1, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.v_button.grid(row=2, column=0, pady=20)
        self.x_button.grid(row=2, column=1, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)
