# Something went wrong : (535, b'5.7.8 Username and Password not accepted. 
# Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials z15sm4180300vsz.27 - gsmtp')
# Means Sign-in attempt was blocked by Google

from getpass import getpass
import smtplib
from email.mime.text import MIMEText##
from email.mime.multipart import MIMEMultipart##
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import date 


def sendEmail(from_email, password, to_email, subject, message, files=[]):
    
    today = date.today()
    
    msg=MIMEMultipart()
    msg['From']= from_email
    msg['To']= to_email
    msg['Subject']= subject + "_" + str(today)
    msg.attach(MIMEText(message, "plain"))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)
    text = msg.as_string()
    try:  
        #server = smtplib.SMTP('smtp.gmail.com', 587) tells smtp what server to use to send email
        server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo() #Extended Simple Mail Transfer Protocol
        #server.starttls() #Starttls turn on encryption, so the email is encrypted between you and Gmail.
        server.login(from_email, password)
        server.sendmail(from_email,to_email,msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Something went wrong : ' + str(e))
        return False
address = getpass("Please enter the email password:   ")
print("Sending email...")
#sendEmail("rachel.lewis9312@gmail.com", address, "rachel.lewis9312@gmail.com","Test", "Hi there, sending this email from Python!", ["Emailmessage.PNG"])

sendEmail("rachel.lewis9312@gmail.com", address, "rachel.lewis9312@gmail.com","Test", "Hi there, sending this email from Python!")
