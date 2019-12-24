import pandas as pd
import smtplib,ssl
import os
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
import config



today = date.today()
contacts=pd.read_excel('emails.xlsx', sheet_name='Sheet1')
username = config.username
password = config.password
subject = "Test"
for i in range(len(contacts)):
    name, email, address = contacts.iloc[i]
    port=465
    smtp_server ='smtp.gmail.com'
    msg=MIMEMultipart()
    msg['From']= username #mycred()[0]
    msg['To']= email
    msg['Subject']= subject + "_" + str(today)
    body = "Hey {}, how is it going? I wanted to confirm your information. Are you still at {}?".format(name.split()[0], address)
    
    msg.attach(MIMEText(body, "plain"))
    text = msg.as_string()
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, msg['To'], text)
    print("Sent to:", name)
print('Done')