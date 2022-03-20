import datetime as dt
import random
import pandas as pd
import smtplib
import os
##### change data types
def read_file():
    date = pd.read_csv("./Birth/birthdays.csv")
    for num_col in date.columns:
        # print(date[num_col].dtypes)
        if date[num_col].dtypes == float:
            date[num_col] = date[num_col].astype("int32")
    return date

##### send an e-mail
def login_email(to_address ,msg):
    my_gmail = "j1@gmail.com"
    gmail_password = "s"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_gmail, password= gmail_password)
        connection.sendmail(from_addr=my_gmail, to_addrs=to_address, msg=f"Subject:Happy Birthday!\n\n{msg}")

##### match date
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today_tuple = (month, day)
 
data = read_file()
matching_data = data[data["month"].isin([month])]
name_list = matching_data["name"].to_list()
email_list= matching_data["email"].to_list()

##### choose a template randomly
template_list = os.listdir("./Birth/letter_templates")
choice = random.choice(template_list)
with open(f"./Birth/letter_templates/{choice}") as date:
    # print(date.read())
    letter_temp = date.read()
    for i, name in enumerate(name_list):
        letter = letter_temp.replace("[NAME]", name)
        for j, email in enumerate(email_list):
            if i == j:
                print(i, j)
                login_email(to_address=email, msg = letter)
