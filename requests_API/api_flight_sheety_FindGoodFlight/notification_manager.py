import os
from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC0bd2928a5eb6edb1e2252288e6ac8369"
        self.auth_token = "19edc731a88d12f54716d6d73e3d6df4"
        # self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    def send_msg(self, price, to_city, to_iata, from_date, to_date):
        self.message = self.client.messages \
                .create(
                     body=f"Only {price} to fly from Incheon-ICN to {to_city}-{to_iata}, from {from_date} to {to_date}.",
                     from_='+13156591997',
                     to='+821090378136'
                 )

if __name__=="__main__":
    noti = NotificationManager()