

import random
# smtplib 用于邮件的发信动作
import smtplib
import string
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header


def genEmailVerifyCode():
    # 生成验证码
    code = ''
    for i in range(6):
        code += random.choice(string.ascii_letters + string.digits)
    return code


def verifyEmail(to_addr: str):
    code = genEmailVerifyCode()
    if sendEmail(to_addr, code):
        return code
    return False


def sendEmail(to_addr: str, verifyCode: str):
    from_addr = '2089647798@qq.com'
    password = 'kbtsfzqjvaxtdaaj'
    smtp_server = 'smtp.qq.com'
    """标题"""
    head = "【四川大学闲鱼】验证码"
    """正文"""
    text = f"【验证码】您的验证码{verifyCode}，该验证码5分钟内有效，请勿泄漏于他人！"
    """邮件内容"""
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(head)
    try:
        # 开启发信服务，这里使用的是加密传输
        # server = smtplib.SMTP_SSL()
        server = smtplib.SMTP_SSL(smtp_server)
        print(server.connect(smtp_server, 465))
        # 登录发信邮箱
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        # 关闭服务器
        server.quit()
        return True
    except:
        return False



