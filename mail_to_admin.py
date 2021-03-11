#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 1:11 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : mail_to_admin.py
# @Software: PyCharm

import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText


def mail_to_admin(**mail_conf):
    """批量发送邮件"""

    msg = MIMEText(mail_conf['mail_context'], 'plain', 'utf-8')
    msg['From'] = mail_conf['my_sender']
    msg['Subject'] = mail_conf['mail_subject']
    server = smtplib.SMTP_SSL(mail_conf['mail_server'], port=mail_conf['port'])

    try:
        server.login(mail_conf['my_sender'], mail_conf['my_pass'])
    except SMTPException as err:
        print("Failed to send mail:{0}".format(str(err)))
    else:
        for recipient in mail_conf['recipients']:
            msg['To'] = recipient
            server.sendmail(mail_conf['my_sender'], recipient, msg.as_string())

    server.quit()
