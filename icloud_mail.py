import smtplib
from email.mime.text import MIMEText
import toml
conf = toml.load(open('config.toml'))
SMTP_SERVER = 'smtp.mail.me.com'
SMTP_PORT = 587

USERNAME = conf["USERNAME"]
PASSWORD = conf["PASSWORD"]

def send_email(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # 使用TLS加密
    server.login(USERNAME, PASSWORD)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def notice():
    title = open('log/article-list.txt').readline().strip()
    for recv in conf["TO"]:
        send_email(conf["FROM"], recv, title, "News from poloniex.")


