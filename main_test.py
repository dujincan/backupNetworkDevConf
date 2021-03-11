#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 1:44 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : main_test.py
# @Software: PyCharm

from mail_to_admin import mail_to_admin
from backup_network_dev import batch_backup_network_dev

mail_context = batch_backup_network_dev('network_device_list.xlsx')

mail_conf = {'my_sender': 'dujc@kuaiche100.cn',
             'my_pass': 'Dida#1..2017',
             'recipients': ["63729988@qq.com", "dujc@kuaiche100.cn"],
             'mail_context': mail_context,
             'mail_subject': '网络设备备份',
             'mail_server': "smtp.exmail.qq.com",
             'port': 465,
             }

mail_to_admin(**mail_conf)
