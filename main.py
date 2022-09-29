#idea: read excel file from sharepoint, send email regarding all expirations in 130 (?) days within work week
#so i run the machine once a week and it will show me all things exp in 130 days from this week
#probabaly set it to compare with a sunday
import email.message

import pandas as pd
import imapclient
import smtplib

pd.read_excel("https://plexusgroupe.sharepoint.com/Shared%20Documents/DP/Property%20&%20Casualty/Executive%20Risk/ER%20BOB.xlsx?web=1")

gmail_imap = "imap.gmail.com"
s= smtplib.SMTP(gmail_imap,587) #this starts the server
s.starttls()
s.ehlo()

password = "plexusbot"
username = "pbotty.uwu@gmail.com"
s.login(username, password)

text = "Expiring policies in this work week: \n"

msg = email.message.EmailMessage()
msg['from']= username
msg['to'] = 'apizano@plexusgroupe.com'
msg['Subject'] = "Expiring Policies Week of: insert week duration"
msg.set_content(text)
res = s.send_message(msg)

