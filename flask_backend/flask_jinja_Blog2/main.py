from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
blog = Post()
blog_data = blog.blog_data

@app.route('/')
def home():
    return render_template("index.html", blog_posts = blog_data)

@app.route('/post/<int:num>')
def get_blog(num):
    return render_template("post.html", num = num, blog_posts = blog_data)
    


if __name__ == "__main__":
    app.run(debug=True)
