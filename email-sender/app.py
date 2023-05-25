#!/usr/bin/env python3

import os
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib


load_dotenv()

email_sender = os.getenv('EMAIL_USERNAME')
email_password = os.getenv('EMAIL_PASSWORD')

email_receiver = 'viresi6427@duscore.com'

subject = 'Dont forget to subsribe'
body = """
When you watch a video, please hit the subsribe button
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
