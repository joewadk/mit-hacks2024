import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()

smtp_server = 'smtp.gmail.com' #using gmail server
smtp_port = 587 #specific port, most email clients use this one
sender_email = os.getenv('email') #gmail
sender_password = os.getenv('password') #app password for above gmail

recipient_email = '+1'+os.getenv('number')+ '@tmomail.net' #note this suffix is only for tmobile
#print(recipient_email) #debug
sms_body = 'Hello, this is a test SMS via email!' #text body

msg = MIMEText(sms_body) #email structure, on mobile sms it shows / <subject/ <body>
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Test SMS'


try:
    with smtplib.SMTP(smtp_server, smtp_port) as server: #server stuff
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("SMS sent!")#it worked! however it might get blocked by carrier after 1 use.
except:
    print('you stupid') 
