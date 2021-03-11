#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 4:51 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : backup_network_dev.py
# @Software: PyCharm

import netmiko
from netmiko import NetMikoTimeoutException, NetMikoAuthenticationException
from datetime import datetime
import time
import xlrd


def backup_network_dev(**device):
    """备份华为和思科网络设备"""

    conf = ''

    try:
        connect_dev = netmiko.ConnectHandler(**device)
        if device['device_type'] == 'huawei':
            connect_dev.send_command('dis arp')
        elif device['device_type'] == 'cisco_ios':
            connect_dev.send_command('show arp')

    except NetMikoAuthenticationException as err_msg:
        return str(err_msg)
    except NetMikoTimeoutException as err_msg:
        return str(err_msg)
    except Exception as err_msg:
        return str(err_msg)

    else:
        if device['device_type'] == 'huawei':
            conf = connect_dev.send_command('dis cu')

        elif device['device_type'] == 'cisco_ios':
            connect_dev.enable()
            conf = connect_dev.send_command('show run')

        now = datetime.now()
        backup_file = "dev_" + device['ip'] + "_" + str(now.year) + str(now.month) \
                      + str(now.day) + str(time.strftime("%H%M")) + ".cfg"
        backup = open(backup_file, "w")
        backup.write(conf)
        backup.close()
        return f"{device['ip']}{' backup successful!'}"


def batch_backup_network_dev(excelfile):
    """批量备份华为或思科网络设备"""

    msg = []

    workbook = xlrd.open_workbook(excelfile)
    sheet = workbook.sheet_by_index(0)

    for device in range(1, sheet.nrows):
        ip = sheet.row(device)[1].value
        port = sheet.row(device)[2].value
        username = sheet.row(device)[3].value
        password = sheet.row(device)[4].value
        secret = sheet.row(device)[5].value
        device_type = sheet.row(device)[6].value

        node = {
            "device_type": device_type,
            "ip": ip,
            "port": port,
            "username": username,
            "password": password,
            "secret": secret,
        }

        output = backup_network_dev(**node)
        print(str(output) + "\n")
        msg.append(output)

    return "\n".join(msg)
