import imaplib
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')

user = input("Enter your email: ")

# Remember , you may need an app password if you are a gmail user
password = getpass.getpass("Enter your password: ")
M.login(user,password)
M.list()

# Connect to your inbox
M.select("inbox")

# Searching Mail

typ ,data = M.search(None,'SUBJECT "this is a test email for python"')

print(typ)
print(data)

result, email_data = M.fetch(data[0],"(RFC822)")

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

import email

email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
  if part.get_content_type() == "text/plain":
    body = part.get_payload(decode=True)
    print(body)
  
# for link in email, replace "text/plain" to "text/html"