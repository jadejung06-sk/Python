from genericpath import exists
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests

class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<Movie %r>' % self.title

db.create_all()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

if not exists('./flask_backend/flask_SQL_WTF_Movies\movie-collection.db'):
    db.session.add(new_movie)   
    db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies = all_movies)

@app.route("/edit", methods = ['GET', 'POST'])
def edit():
    movieform = RateMovieForm()
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    if request.method == 'POST' and movieform.validate_on_submit():
        db.update(Movie).where(Movie.id)
        return redirect(url_for('home'))
    # return render_template('edit.html')
    
    return render_template("edit.html", form = movieform, movie = movie_selected)  

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/select")
def select():
    pass

if __name__ == '__main__':
    app.run(debug=True)