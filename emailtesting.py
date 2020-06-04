import smtplib
from password import password

sender = 'conordurkin@me.com'
receiver = 'conordurkin@me.com'

message_opening = """From: Conor <conordurkin@me.com>
To: Conor <conordurkin@me.com>
Subject: Muirfield has an opening!

Hi there - Muirfield has an opening for you!
Go check it rather quickly before someone else snatches it up:

https://www.muirfield.org.uk/visitors/?date=05/13/2021#booking

Good luck.

"""

message_running = """From: Conor <conordurkin@me.com>
To: Conor <conordurkin@me.com>
Subject: Still running.

Nothing yet on Muirfield. Will keep checking.

"""

# If time opens up, send me the "Opening exists" email, then stop checking the site.
smtpObj = smtplib.SMTP('smtp.mail.me.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('conordurkin@me.com', password)
smtpObj.sendmail(sender, receiver, message_opening)
smtpObj.quit()
print("Opening exists email sent")

smtpObj = smtplib.SMTP('smtp.mail.me.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('conordurkin@me.com', password)
smtpObj.sendmail(sender, receiver, message_running)
smtpObj.quit()
print("Still running email sent")
