from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import requests

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

@app.route("/")
def home():
    return render_template("index.html")
    
## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe = dict(id = random_cafe.id, name = random_cafe.name, map_url = random_cafe.map_url, 
    img_url = random_cafe.img_url,
    location = random_cafe.location,
    seats = random_cafe.seats,
    has_toilet = random_cafe.has_toilet,
    has_wifi = random_cafe.has_wifi,
    has_sockets = random_cafe.has_sockets,
    can_take_calls = random_cafe.can_take_calls,
    coffee_price =random_cafe.coffee_price))
  
@app.route('/all')
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for ca in cafes:
        cafe_list.append(dict(id = ca.id, name = ca.name, map_url = ca.map_url, 
    img_url = ca.img_url,
    location = ca.location,
    seats = ca.seats,
    has_toilet = ca.has_toilet,
    has_wifi = ca.has_wifi,
    has_sockets = ca.has_sockets,
    can_take_calls = ca.can_take_calls,
    coffee_price = ca.coffee_price))
    return jsonify(cafe = cafe_list)

### trial 1
# @app.route('/search')
# def  get_cafe_at_location():
#     params = {'lat' : , 'lon' : }
#     request.get('http://api.open-notify.org/iss-pass.json', params=params)
#     return redirect(url_for('search_loc', loc = ))


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
