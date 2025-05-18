import os
from email.mime.text import MIMEText
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, message):
    msg = MIMEText(message)
    msg["Subject"] = "Notification"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())

def send_sms(to_number, message):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
    client.messages.create(body=message, from_=os.getenv("TWILIO_PHONE"), to=to_number)
