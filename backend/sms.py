import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()

def send_sms(recipient_email, sms_body):
    smtp_server = 'smtp.gmail.com' #using gmail server
    smtp_port = 587 #specific port, most email clients use this one
    sender_email = os.getenv('email') #gmail
    sender_password = os.getenv('password') #app password for above gmail

     #recipient_email = '+1'+os.getenv('number')+ '@tmomail.net' #note this suffix is only for tmobile
    recipient_email = 'asbcascacs@ishmamf.com'
    sms_body = 'Hello, this is a test SMS via email!' #text body

    msg = MIMEText(sms_body) #email structure, on mobile sms it shows / <subject/ <body>
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Test SMS'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        return "SMS sent!"
    except Exception as e:
        return str(e)

