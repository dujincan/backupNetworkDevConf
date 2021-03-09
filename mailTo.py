#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 1:11 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : mailTo.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def mailto(my_sender, my_pass, recipients, mail_context, mail_subject, mail_server, port):
    for recipient in recipients:
        try:
            msg = MIMEText(mail_context, 'plain', 'utf-8')
            msg['From'] = formataddr([" ", my_sender])
            msg['To'] = formataddr([" ", recipient])
            msg['Subject'] = mail_subject

            server = smtplib.SMTP_SSL(mail_server, port=port)
            server.login(my_sender, my_pass)
            server.sendmail(my_sender, recipient, msg.as_string())
            server.quit()
        except Exception as err:
            print(err)

