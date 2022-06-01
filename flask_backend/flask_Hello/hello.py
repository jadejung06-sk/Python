from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
        '<p>This is a paragraph.</p>'\
            '<img src="https://media.giphy.com/media/Puc4FZWExJc0E/giphy.gif" width=200>'

### trial 3
def make_bold(function):
    function()
    return f"<b></b>"

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"

# @app.route("/username/<name>/<int:number>")
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


### trial 1
# @app.route("/bye")
# def make_bold(text):
#     return f'<b>{text}</b>'
# @app.route("/bye")
# def make_emphasis(text):
#     return f'<em>{text}</em>'
# @app.route("/bye")
# def make_underlined(text):
#     return f'<u>{text}</u>'

### trial 2
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# @app.route("/bye")
# def bye():
#     return "Bye!"
# @make_emphasis
# @make_underlined
# def bye():
#     return "<u><em><b>Bye!</b></em></u>"



if __name__=="__main__":
    app.run(debug=True)

# on ps $env:FLASK_APP = "./flask_backend/flask_Hello/hello.py"
# on ps flask run
# http://127.0.0.1:5000/