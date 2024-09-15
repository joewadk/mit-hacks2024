import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

# Function to query medications for the morning (6AM to 11AM)
def query_morning_medications():
    try:
        con = psycopg2.connect(
            host=os.getenv('db_host'),
            database=os.getenv('db_database'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            port=5432
        )

        cur = con.cursor()

        # SQL query to find medications to take in the morning (6AM to 11AM)
        query = """
            SELECT prescription_name, raw_instruction
            FROM jawad
            WHERE (EXTRACT(HOUR FROM expected_time1) BETWEEN 6 AND 11)
            OR (EXTRACT(HOUR FROM expected_time2) BETWEEN 6 AND 11)
            OR (EXTRACT(HOUR FROM expected_time3) BETWEEN 6 AND 11);
        """
        cur.execute(query)
        rows = cur.fetchall()

        # Close the cursor and connection
        cur.close()
        con.close()

        return rows

    except Exception as e:
        print(f"An error occurred while querying morning medications: {e}")

# Function to send SMS via email
def send_sms(recipient_email, sms_body):
    recipient_email = '+1'+os.getenv('number')+ '@tmomail.net' #note this suffix is only for tmobile
    smtp_server = 'smtp.gmail.com' #using gmail server
    smtp_port = 587 #specific port, most email clients use this one
    sender_email = os.getenv('email') #gmail
    sender_password = os.getenv('password') #app password for above gmail

    msg = MIMEText(sms_body) #email structure, on mobile sms it shows / <subject/ <body>
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Morning Medications Reminder'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        return "SMS sent!"
    except Exception as e:
        return str(e)

# Main function to query medications and send SMS
def send_morning_medication_reminder(recipient_email):
    morning_medications = query_morning_medications()

    if not morning_medications:
        print("No morning medications found.")
        return

    # Create the SMS body with the list of medications
    sms_body = "You have the following medications to take this morning:\n"
    for med in morning_medications:
        sms_body += f"- {med[0]}: {med[1]}\n"

    # Send the SMS via email
    result = send_sms(recipient_email, sms_body)
    print(result)

# Example usage
send_morning_medication_reminder('asbcascacs@ishmamf.com')
