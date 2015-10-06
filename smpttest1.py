__author__ = 'Administrator'
from email.mime.text import MIMEText
msg=MIMEText('hello,send by python...','plain','utf-8')

from_addr='shadowlaser@hotmail.com'
password='19880830'
to_addr='674925643@qq.com'
smtp_server='smtp.live.com'
import smtplib
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr=input('From:')
password=input('Password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')

msg=MIMEText('hello,send by Python...','plain','utf-8')
msg['From']=_format_addr('python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自smtp的问候...','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail((from_addr,[to_addr],msg.as_string()))
server.quit()



msg=MIMEMultipart()
msg['From']=''
msg['To']=''
msg['Subject']=''

msg.attach(MIMEText('dsfds','plain','utf-8'))
with open('/user/test.png','rb') as f:
    mime=MIMEBase('image','png',filename='test.png')
    mime.add_header('Content-Disposition','attachment',filename='test.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)



