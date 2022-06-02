from flask import Flask, render_template
import random
import datetime
import requests

## Guess a gender
def guess_gen(name):
    gen_url = f'https://api.genderize.io?name={name}'
    gen_response = requests.get(gen_url)
    output_name = gen_response.text['name']
    output_gen = gen_response.text['gender']
    return output_gen

## Guess an old
def guess_old(name):
    old_url = f'https://api.agify.io?name={name}'
    old_response = requests.get(old_url)
    _name = old_response.text['name']
    output_old = old_response.text['age']
    return output_old

app = Flask(__name__)
@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess():
    return 


if __name__=="__main__":
    app.run(debug=True)
    
    