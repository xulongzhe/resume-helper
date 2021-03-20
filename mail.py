import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:

    def __init__(self, sender, smtpserver, username, password):
        self.sender = sender
        self.smtpserver = smtpserver
        self.username = username
        self.password = password

    def send(self, receivers: list, title, content, attaches=None):
        if attaches is None:
            attaches = []
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = ','.join(receivers)
        message['Subject'] = Header(title, 'utf-8')

        message.attach(MIMEText(content, 'html', 'utf-8'))

        for attach in attaches:
            file = open(attach, 'rb')
            payload = MIMEApplication(file.read())
            payload.add_header('Content-Disposition', 'attachment',
                               filename=os.path.basename(file.name))
            message.attach(payload)

        smtpObj = smtplib.SMTP_SSL(self.smtpserver)
        smtpObj.connect(self.smtpserver)
        smtpObj.login(self.username, self.password)
        smtpObj.sendmail(self.sender, receivers, message.as_string())
        smtpObj.quit()
