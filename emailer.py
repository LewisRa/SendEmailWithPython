# Something went wrong : (535, b'5.7.8 Username and Password not accepted. 
# Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials z15sm4180300vsz.27 - gsmtp')
# Means Sign-in attempt was blocked by Google

from getpass import getpass
import smtplib
from email.mime.text import MIMEText##
from email.mime.multipart import MIMEMultipart##
from email.mime.base import MIMEBase
from email import encoders


def sendEmail(from_email, password, to_email, subject, message):
    msg=MIMEMultipart()
    msg['From']= from_email
    msg['To']= to_email
    msg['Subject']= subject

    msg.attach(MIMEText(message, "plain"))
    try:  
        #server = smtplib.SMTP('smtp.gmail.com') 
        server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo() #Extended Simple Mail Transfer Protocol
        server.login(from_email, password)
        server.sendmail(from_email,to_email,msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Something went wrong : ' + str(e))
        return False
address = getpass("Please enter the email password:   ")
print("Sending email...")
sendEmail("rachel.lewis9312@gmail.com", address, "rachel.lewis9312@gmail.com","Test", "Hi there, sending this email from Python!")
