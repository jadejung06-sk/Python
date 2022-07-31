from site import USER_BASE
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from numpy import NaN
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.exc import IntegrityError
import sqlite3

app = Flask(__name__)


app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# db.create_all()

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

### trial 1
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         no_hashed_password = request.form.get('password')
#         new_email = request.form.get('email')
#         # old_user = db.session.execute("SELECT email from User where email= :val", {'val': new_email})
#         # print(old_user)
#         hashed_password = generate_password_hash(no_hashed_password, method='pbkdf2:sha256', salt_length=8)
#         try:
#             new_user = User(
#         name = request.form.get('name'),
#         email = new_email,
#         password = hashed_password
#         )
#         except sqlite3.IntegrityError as err:
#             error = "You've already signed up with that email."
#             return render_template('login.html', error=error)
#         except IntegrityError as err:
#             error = "You've already signed up with that email."
#             return render_template('login.html', error=error)
#         db.session.add(new_user)
#         db.session.commit()
#         login_user(new_user)
#         return redirect(url_for('secrets'))    
    # return render_template("register.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        if User.query.filter_by(email=request.form.get('email')).first():
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


### trial 1
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = User.query.filter_by(email=email).first()
#         error = 'Invalid credentials'
#         if user != None and check_password_hash(user.password, password):
#             login_user(user)
#             return redirect(url_for('secrets'))
#         elif check_password_hash(user.password, password) == False:
#             error = 'Password incorrect, please try again.'
#             return render_template('login.html', error=error)
#         return render_template('login.html', error=error)
#     return render_template('login.html', error=error)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
    
        user = User.query.filter_by(email=email).first()
        #Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        #Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        #Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route('/secrets')
@login_required
def secrets():    
    print(current_user)
    return render_template("secrets.html", name= current_user.name, logged_in = True)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    # print(os.path.join(os.getcwd(),'flask_backend/flask_auth/static/files/'))
    # return send_from_directory(os.path.join(os.getcwd(),'flask_backend/flask_auth/static/files'), 'cheat_sheet.pdf')
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)


