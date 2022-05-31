from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


    # on ps $env:FLASK_APP = "./flask_backend/flask_Hello/hello.py"
    # on ps flask run
    # http://127.0.0.1:5000/

if __name__=="__main__":
    app.run()