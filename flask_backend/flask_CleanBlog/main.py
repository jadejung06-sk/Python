from flask import Flask, render_template, url_for
import requests
import datetime

#  August 24, 2022
date = datetime.datetime.now().strftime('%B %d, %Y')
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts, date = date)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:number>")
def get_post(number):
    return render_template("post.html", all_posts=posts, number = number, date = date)


if __name__=="__main__":
    app.run(debug=True)

