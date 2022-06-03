from flask import Flask, render_template
import random
import datetime
import requests
import json

## Guess a gender
def guess_gen(name):
    gen_url = f'https://api.genderize.io?name={name}'
    gen_response = requests.get(gen_url)
    gen_dict = json.loads(gen_response.text)
    output_gen = gen_dict['gender']
    return output_gen

## Guess an old
def guess_old(name):
    old_url = f'https://api.agify.io?name={name}'
    old_response = requests.get(old_url)
    old_dict = old_response.json() # ★
    output_old = old_dict['age']
    return output_old

app = Flask(__name__)
@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<your_name>')
def guess(your_name):
    your_gender = guess_gen(your_name)
    your_old = guess_old(your_name)
    return render_template('guess.html', your_name = your_name, your_gender = your_gender, your_old = your_old)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts = all_posts)

if __name__=="__main__":
    app.run(debug=True)
