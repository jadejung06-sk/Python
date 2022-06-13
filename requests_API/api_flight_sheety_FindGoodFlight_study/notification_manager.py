import os
from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = ""
        self.auth_token = ""
        # self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    def send_msg(self, price, to_city, to_iata, from_date, to_date):
        self.message = self.client.messages \
                .create(
                     body=f"Only {price:,} won to fly from Incheon-ICN to {to_city}-{to_iata}, from {from_date} to {to_date}.",
                     from_='+13',
                     to='+8210'
                 )

# if __name__=="__main__":
#     noti = NotificationManager()
