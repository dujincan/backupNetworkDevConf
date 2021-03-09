#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 1:56 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : main.py
# @Software: PyCharm

from backup import backup_network_device
from mailTo import mailto

# backup
excel_file = 'xxxxxxx.xlsx'
backup_dir = '/xxxxxxx/backup/'
msg = backup_network_device(excel_file, backup_dir)


# send mail
my_sender = "xxxxxxx"
my_pass = "xxxxxxx"
recipients = ["xxxxxxx01", "xxxxxxx02"]
mail_context = msg
mail_subject = "xxxxxxx"
mail_server = "xxxxxxx.com"
port = 465

mailto(my_sender, my_pass, recipients,
       mail_context, mail_subject, mail_server, port)
