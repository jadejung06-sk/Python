from flask import Flask, render_template, request
import requests
import smtplib

def _send_email(msg):
    # msg = "Subject:Hello.\n\nThis is the body of my email"
    my_naver = "jjs0615@naver.com"
    my_gmail = "jongseok.test.01@gmail.com"
    gmail_password = input("Type your password:")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_gmail, password= gmail_password)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_naver, msg=f"Subject:New Message\n\n{msg}")



posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/contact")
# def contact():
    # return render_template("contact.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        msg = f"Subject:New Message.\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n"
        _send_email(msg=msg)
        # return "<h1>Successfully sent your message</h1>"
        return render_template("contact.html",  msg_sent=True)
    return render_template("contact.html",  msg_sent=False)
    



if __name__ == "__main__":
    app.run(debug=True)
