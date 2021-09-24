import requests
import datetime
import smtplib
import time

from bs4 import BeautifulSoup

# KEYBOARD-INFO

keyboard_endpoint = "https://www.amazon.com/Mechanical-Keyboard-Gaming-Keycaps-Computer/dp/B085ZDXGZW/ref=sr_1_10?crid=V9BFTBZKXM4S&dchild=1&keywords=mechanical%2Bkeyboard&qid=1632459243&sprefix=mechanical%2Caps%2C235&sr=8-10&th=1"
# visit "http://myhttpheader.com/" to supply your params below
header = {
    'User-Agent':"Enter Agent Info Here",
    'Accept-Language': "Enter Computer Langauge Here"
}
response = requests.get("https://www.amazon.com/Mechanical-Keyboard-Gaming-Keycaps-Computer/dp/B085ZDXGZW/ref=sr_1_10?crid=V9BFTBZKXM4S&dchild=1&keywords=mechanical%2Bkeyboard&qid=1632459243&sprefix=mechanical%2Caps%2C235&sr=8-10&th=1", headers=header)
html_page = response.text
soup = BeautifulSoup(html_page, 'html.parser')
keyboard_pricing = soup.find('span', 'a-size-medium a-color-price').text
keyboard_int = keyboard_pricing.split("$")[1]

# EMAILING STAGE
MY_EMAIL = "enter email here"
MY_PASSWORD = "enter password here"

time = datetime.datetime.now()

scheduled_message_time = time.strftime('%I:%M%p')

if scheduled_message_time == "11:14PM":
    # EMAIL CLIENT ABOUT PRICING IF IT MEETS STANDARDS== MAKE ANOTHER IF STATEMENT ON PRICING
    #     V V V make sure you use the correct smtp "host key" for example gmail will be "smtp.gmail.com", and yahoo "smtp.mail.yahoo.com" etc, and also remove the high security level on your account setting
#     or elseit won't work
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs='carlos.oran15@hotmail.com', msg="Hello this is a test mail, thanks")
    print('*'*60)
    print('mail has been sent')
    print('*'*60)
else:
    # EMAIL CLIENT -- MAYBE PASS IF AGREED UPON
    print('*'*60)
    print("time has not yet been fulfilled")
    print('*'*60)   
