from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0,9)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=500>"

### trial 1
# def question_num(guess):
#     guess = int(input("Guess a single number."))
#     ans = random.randint(0,9)
#     if guess < ans:
#         return "<h1 style='color:red;'>Too low, try again!<h1>"
#     elif guess == ans:
#         return "<h1 style='color:red;'>You found me!<h1>"
#     else:
#         return "<h1 style='color:blue;'>Too high, try again!<h1>"
### trial 2
# def answer_num():
#     def wrapper(function):
#         return function() >= int(input("Guess a single number"))
#     return wrapper

### trial 3
# def answer():
#     return random.randint(0,9)
# @app.route('/answer')
# def answer_num(answer):
#     answer = random.randint(0,9)
#     def wrapper(function):
#         if answer 
#         return  
#     return wrapper

@app.route('/<int:number>')
def check_answer(number):
    if number < random_number:
        return "<h1 style='color:red;'>Too low, try again!<h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=500>"
    elif number == random_number:
        return "<h1 style='color:red;'>You found me!<h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=500>"
    else:
        return "<h1 style='color:blue;'>Too high, try again!<h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=500>"

if __name__=="__main__":
    app.run(debug=True)