import smtplib

# Provider	SMTP server domain name
# Gmail (will need App Password)	smtp.gmail.com
# Yahoo Mail	smtp.mail.yahoo.com
# Outlook.com/Hotmail.com	smtp-mail.outlook.com
# AT&T	smpt.mail.att.net (Use port 465)
# Verizon	smtp.verizon.net (Use port 465)
# Comcast	smtp.comcast.net

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
 
# For hidden passwords
import getpass

# Note for Gmail Users, you need to generate an app password instead of your normal email password. This also requires enabling 2-step authentication. Follow the instructions here to set-up 2-Step Factor Authentication as well as App Password Generation:https://support.google.com/accounts/answer/185833?hl=en/. Set-up 2 Factor Authentication, then create the App Password, choose Mail as the App and give it any name you want. This will output a 16 letter password for you. Pass in this password as your login password for the smtp.

email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)

from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()