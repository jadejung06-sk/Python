import smtplib
import random
import datetime as dt

##### login e-mail
def login_email(msg):
    # msg = "Subject:Hello.\n\nThis is the body of my email"
    my_naver = "jjs0615@naver.com"
    my_gmail = "j1@gmail.com"
    gmail_password = "s"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_gmail, password= gmail_password)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_naver, msg=f"Subject:Monday Motivation\n\n{msg}")

##### check a monday
##### read a line
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6: # 6 sunday 0 monday
    with open("./Birth/quotes.txt") as quote:    
        all_quotes = quote.readlines() # to_list
        quote = random.choice(all_quotes)
    print(quote)
    login_email(msg= quote)