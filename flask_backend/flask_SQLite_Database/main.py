from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
##### sqlite3 case
# db = sqlite3.connect("./flask_backend/flask_SQLite_Database/new-books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

##### SQLAlchemy case
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////flask_backend/flask_SQLite_Database/new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

book = books()
# books = books(id=1, title='Harry Potter', author='J. K. Rowling', review=9.3 )

all_books = [     

    ]

@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = {
            'title' : request.form['title'],
            'author':request.form['author'],
            'rating': request.form['rating']
        }
        all_books.append(new_book)
        return redirect(url_for('home')) # 
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

