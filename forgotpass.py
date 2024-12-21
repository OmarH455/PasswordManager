import smtplib
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self, from_email="rcuocpcigt43@iockn.eqo", from_password="homv Adgc osAk sfvA",encryption_instance=None):
        self.smtp_server = "smtp.gmail.com"
        self.port = 465
        self.encryption = encryption_instance
        self.from_email = self.encryption.decrypt(from_email)
        self.from_password = self.encryption.decrypt(from_password)

    def send_password_email(self):
        with open("users.txt", 'r') as file:
            lines = file.readlines()
            password = self.encryption.decrypt(lines[0].strip().split(" | ")[1])
            to_email = lines[0].strip().split(" | ")[0]
        subject = "Your Password Recovery"
        body = f"Your password is: {password}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.from_email
        msg['To'] = to_email
        

        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
                server.login(self.from_email, self.from_password)
                server.sendmail(self.from_email, to_email, msg.as_string())
            return True
        except Exception as e:
            return e

#example

