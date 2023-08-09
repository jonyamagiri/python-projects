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
# email_receiver = '****'

subject = 'Welcome to Our Newsletter!'
body = """
Dear Subscriber, 
 
We are so excited that you have subscribed to our newsletter! We look forward to providing you with the latest news and updates. With your subscription, we will keep you informed of upcoming events and opportunities in our community.  

At iCreate, we strive for excellence in everything we do from customer service to product quality. We value your trust and loyalty, which is why its important for us that each subscriber receives only the best information available.  

If there is ever anything else that we can do for you or if theres something specific about which would like more information on please don't hesitate reach out at any time -we're always here help!   

Thanks again for subscribing; enjoy all of the great content coming your way soon!.    

Sincerely,  iCreate Team
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
