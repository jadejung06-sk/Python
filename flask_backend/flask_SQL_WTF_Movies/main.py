from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests

class MovieForm(FlaskForm):
    rating = IntegerField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    moviename = db.Column(db.String(80), unique=True, nullable=False)
    movierating = db.Column(db.Integer)
    moviereview = db.Column(db.String(120), unique=True, nullable=False)
    moviestory = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<Movie %r>' % self.moviename

db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/edit")
def edit():
    movieform = MovieForm()
    return render_template("edit.html", form = movieform)

    

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/select")
def select():
    pass

if __name__ == '__main__':
    app.run(debug=True)
