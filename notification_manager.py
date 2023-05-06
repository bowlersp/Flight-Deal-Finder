import smtplib

MY_EMAIL = "pythonburner1980@gmail.com"
MY_PASSWORD = "1qaz2wsx!QAZ@WSX"

class NotificationManager:

    def send_email(self):
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Low Price Alert On Flights!\n\n "
            )

