# Desde maio de 2022 o Google desabilitou o acesso de apps terceiros a conta google sem uma senha
# especifica de acesso

import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "53NhAI2E"
subject = "Python email test"
body = "I wrote a email :D"

# header
message = f"""From: Marcos Silva{sender}
To: Marcos Dorneles{receiver}
Subject: {subject}
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in ...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in :(")
