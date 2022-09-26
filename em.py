import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
def email(em, sub, bod, fname):
    dir = os.path.dirname(os.path.realpath(__file__))+"/data/"
    fromaddr = "iamthesender007@gmail.com"
    toaddr = em
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = sub
    body = bod
    msg.attach(MIMEText(body, 'plain'))
    filename = fname
    attachment = open(dir+filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "kbogqctuecrcprks")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
