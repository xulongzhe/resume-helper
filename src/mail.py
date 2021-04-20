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
            payload.add_header('Content-Type','application/octet-stream')
            payload.add_header('Content-Disposition', 'attachment',
                               filename=Header(os.path.basename(file.name), 'utf-8').encode())
            message.attach(payload)

        smtpObj = smtplib.SMTP_SSL(self.smtpserver)
        smtpObj.connect(self.smtpserver)
        smtpObj.login(self.username, self.password)
        smtpObj.sendmail(self.sender, receivers, message.as_string())
        smtpObj.quit()

if __name__ == '__main__':
    email_sender = 'tel15258826527@sina.com'
    email_password = '337413c8324ffb81'
    email_smtp_sever = 'smtp.sina.com'
    m = Email(email_sender, email_smtp_sever, email_sender, email_password)
    m.send(['xulongzhe@uniview.com'], '2021-04-19 22:38 收到 杭州Java正式 简历1份', '2021-04-19 22:38 收到 杭州Java正式 简历1份', ['/home/xulongzhe/下载/滴滴电子发票 (2).pdf'])
    