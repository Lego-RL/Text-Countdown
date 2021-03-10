from datetime import date
import schedule
import smtplib
import time


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('email', 'password')

from_mail = 'email'
to_mail = 'xxxxxxxxxx@vtext.com' #phone number @vtext.com for verizon, different for other carriers


def get_days_left():
    d0 = date.today()
    d1 = date(2021, 5, 14) #last day of my spring semester

    delta = d1-d0
    return delta.days


def build_message(msg):
    #message wouldn't appear unless formatted in this way I found in a github issue
    return ("From: %s\r\n" % from_mail + "To: %s\r\n" % to_mail + "Subject: %s\r\n" % '' + "\r\n" + msg)


def send_text():
    message = f'There are only {get_days_left()} days left until the end of the spring semester!'

    message = build_message(message)
    server.sendmail(from_mail, to_mail, message)


schedule.every().day.at('16:00').do(send_text)

while True:
    schedule.run_pending()
    time.sleep(1)