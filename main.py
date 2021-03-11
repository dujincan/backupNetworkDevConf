#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 1:56 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : main.py
# @Software: PyCharm

from mail_to_admin import mail_to_admin
from backup_network_dev import batch_backup_network_dev

mail_context = batch_backup_network_dev('xxxxxxx.xlsx')

mail_conf = {'my_sender': 'xxxxx@xxxxxxxxx.com',
             'my_pass': 'xxxxxxx',
             'recipients': ["xxxxxxx", "xxxxxxx"],
             'mail_context': mail_context,
             'mail_subject': 'xxxxxxx',
             'mail_server': "xxxxxxx",
             'port': 465,
             }


mail_to_admin(**mail_conf)


