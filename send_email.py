import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "santanudas229933@gmail.com"
    password = os.getenv('PASSWORD')

    context = ssl.create_default_context()

    receiver = "santanudas229933@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)