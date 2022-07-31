from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label = 'Email', validators=[DataRequired(), Email()])
    password = PasswordField(label = 'Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = 'lajdfjaiojfojaoi'
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # print(type(login_form.password.data))
        if login_form.email.data == "admin@email.com" and int(login_form.password.data) == 12345678 : # 
            return render_template('success.html')
        else :
            return render_template('denied.html')
    return render_template('login.html', form = login_form)

# @app.route("/cafes", methods=['GET', 'POST'])
# def cafes():
#     return render_template("cafes.html")


if __name__ == '__main__':
    app.run(debug=True)



