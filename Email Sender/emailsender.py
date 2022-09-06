from email.message import EmailMessage
from password import email_password
import ssl
import smtplib

email_sender = 'lakshit510@gmail.com'
email_sender_password = email_password

email_receiver = 'luckyhacker017@gmail.com'

email_subject = 'Python Project test Email'

email_body = """
Hello this is Lakshit from lakshit510 mail id 
mailing a test mail to luckyhacker for a Python Project testing
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_sender_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())