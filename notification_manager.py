import smtplib
from twilio.rest import Client

### EMAIL CREDS ###

MY_EMAIL = "pythonburner1980@gmail.com"
MY_PASSWORD = "1qaz2wsx!QAZ@WSX"

### TWILIO CREDS ###

TWILIO_SID = "AC411550bdd17bd9996aefbd092d3c91f1"
TWILIO_AUTH_TOKEN = "137c40719d047129f6be94e04df7e5d0"
TWILIO_VIRTUAL_NUMBER = "18442923991"
TWILIO_VERIFIED_NUMBER = "16185415179"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        # Prints if successfully sent.
        print(message.sid)


    # def send_email(self):
    #     with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         connection.sendmail(
    #             from_addr=MY_EMAIL,
    #             to_addrs=MY_EMAIL,
    #             msg=f"Subject: Low Price Alert On Flights!\n\n "
    #         )



