#pip install smtplib
#pip install MyHall

from http import server
import smtplib
from email.message import EmailMessage
x = "robscherer123@gmail.com"
y = 1000

def email_alert(subject, body, to):

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to



    user = "pfood7832@gmail.com"
    msg['from'] = user
    password = "hkhvwkqcmvrpxljr"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
if _name_ == '_main_':
    
    for i in range(y):
            print("\nSending Mail to", x, "...")

            email_alert("Helmet-Heroes Banned Appeal", "Hello good day Mr.Robby almost 3months Its me again IGN: xxNightFury almost 3 months my accout banned, Im sorry for spaming you a email about my account i just want my account back because my account got banned the reason is (Pet money dupe attempt.) I dont know what i do i deposit my money and teleport to petshop and buy some pet and after i purchase i got disconnected 😭 I think I perform a expired/fixed dupe method. Please Mr.Robby unbanned my account IGN: xxNightFury thats my only account🥺 i hope you respond my report.", x)
    
            print(i, "(Sent Succsessfully!!)"