from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import random

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


### trial 2
# @app.route('/search')
# def  get_cafe_at_location():
#     params = {'lat' : 50, 'lon': -5}
#     response = requests.get('http://api.open-notify.org/iss-pass.json', params=params)
#     if response.json()['message'] == 'failure':
#         return jsonify(error = {'Not Found' : "Sorry, we don't have a cafe at that location."})
#     return response.json()

### trial 3
@app.route('/search')
def get_cafe_at_location():
    query_location = request.args.get('loc')
    first_cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if first_cafe:
        return jsonify(cafe = dict(id = first_cafe.id, name = first_cafe.name, map_url = first_cafe.map_url, 
    img_url = first_cafe.img_url,
    location = first_cafe.location,
    seats = first_cafe.seats,
    has_toilet = first_cafe.has_toilet,
    has_wifi = first_cafe.has_wifi,
    has_sockets = first_cafe.has_sockets,
    can_take_calls = first_cafe.can_take_calls,
    coffee_price =first_cafe.coffee_price))
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

## HTTP POST - Create Record
@app.route('/add', methods= ['POST'])
def post_new_cafe():
    api_key = request.args.get("api-key")
    if api_key == 'TopSecretAPIKey':
        new_cafe = Cafe(
            name = request.form.get('name'),
            map_url = request.form.get('map_url'),
            img_url = request.form.get('img_url'),
            location=request.form.get("loc"),
            has_sockets = bool(request.form.get('sockets')),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"))
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response = {'success' : 'Successfully added the new cafe.'})

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        print(cafe)
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"Sucesss" : "Successfully updated the price."}), 200
    return jsonify(error = {'Not Found' : 'Sorry a cafe with that id was not found in the database.'}), 404

## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods= ['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == "TopSecretAPIKey":
        deleted_cafe = Cafe.query.get(cafe_id) # PK
        if deleted_cafe:
            print(deleted_cafe)
            db.session.delete(deleted_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error = {'Not Found' : 'Sorry a cafe with that id was not found in the database.'}), 404
    return jsonify({"error" : "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
    # params = {'lat' : 50, 'lon': -500}
    # response = requests.get('http://api.open-notify.org/iss-pass.json', params=params)
    # print(response.json()['message'] == 'failure')