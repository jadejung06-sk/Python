from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os


app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(250))
    name = db.Column(db.String(1000))
    is_authenticated = db.Column(db.Boolean, default=False, nullable=False)
#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        no_hashed_password = request.form.get('password')
        hashed_password = generate_password_hash(no_hashed_password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(
        name = request.form.get('name'),
        email = request.form.get('email'),
        password = hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets'))
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    last_user = User.query.order_by(User.id.desc()).first()
    return render_template("secrets.html", name= last_user.name)


@app.route('/logout')
def logout():
    pass


# @app.route('/download')
# def download():
#     pass

@app.route('/download')
def download():
    # print(os.path.join(os.getcwd(),'flask_backend/flask_auth/static/files/'))
    # return send_from_directory(os.path.join(os.getcwd(),'flask_backend/flask_auth/static/files'), 'cheat_sheet.pdf')
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)


