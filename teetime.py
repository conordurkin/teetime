import requests
from bs4 import BeautifulSoup
import smtplib
import time as t

# I have a separate file entitled 'password.py' with one line of code containing a password to my @me.com account (password = 'XYZ').
from password import password

# Keep track of how many times program runs
counter = 0

# Define the info for the email messages I'm sending.
sender = 'conordurkin@me.com'
receiver = 'conordurkin@me.com'

message_opening = """From: <conordurkin@me.com>
To: <conordurkin@me.com>
Subject: Muirfield has an opening!

Hi there - Muirfield has an opening for you!
Go check it rather quickly before someone else snatches it up:

https://www.muirfield.org.uk/visitors/?date=05/13/2021#booking

Good luck.

"""

message_running = """From: <conordurkin@me.com>
To: <conordurkin@me.com>
Subject: Muirfield app is still running.

Nothing yet on Muirfield. Will keep checking.

"""

while True:

    # This is the code to check the website - if len(free) > 0, then a tee time is available.
    page = requests.get("https://www.muirfield.org.uk/visitors/?date=05/13/2021#booking")
    soup = BeautifulSoup(page.content, features = 'html.parser')
    free = soup.find_all('td', string = "Yes")
    booked = soup.find_all('td', string = "No")
    len(free)
    len(booked)
    counter += 1

    if len(free) > 0:
    # If time opens up, send me the "Opening exists" email, then stop checking the site.
        smtpObj = smtplib.SMTP('smtp.mail.me.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('conordurkin@me.com', password)
        smtpObj.sendmail(sender, receiver, message_opening)
        smtpObj.quit()
        break

    elif counter % 1969 == 0:
    # Code takes ~5-8 seconds to run, then sleeps for 5 minutes. Roughly once per week (every 1969 times), sends me email letting me know it's still runing.
        smtpObj = smtplib.SMTP('smtp.mail.me.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('conordurkin@me.com', 'lhad-xtzr-rdtu-pqrt')
        smtpObj.sendmail(sender, receiver, message_running)
        smtpObj.quit()
        print(f"Ran loop number {counter} at ", t.asctime())
        t.sleep(300)

    else:
    # If no times, wait 5 minutes, then check again.
        print(f"Ran loop number {counter} at ", t.asctime())
        t.sleep(300)
