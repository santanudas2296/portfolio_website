import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "santanudas229933@gmail.com"
    password = "zqmndmnaqmiktlmj"

    context = ssl.create_default_context()

    receiver = "santanudas229933@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)