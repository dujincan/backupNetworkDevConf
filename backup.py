#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 11:08 上午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : backupNetworkDeviceConfig.py
# @Software: PyCharm

import paramiko
import xlrd
import time
from datetime import datetime
from pprint import pprint


def backup_network_device(excel_file, backup_dir):
    msg = []

    workbook = xlrd.open_workbook(excel_file)
    sheet = workbook.sheet_by_index(0)

    for index in range(1, sheet.nrows):
        hostname = sheet.row(index)[0].value
        ipaddr = sheet.row(index)[1].value
        username = sheet.row(index)[2].value
        password = sheet.row(index)[3].value
        enable_password = sheet.row(index)[4].value
        vender = sheet.row(index)[5].value

        try:
            pprint(str(datetime.now()) + " Saving config from device {0}".format(hostname))
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ipaddr, username=username, password=password, look_for_keys=False)
            command = ssh_client.invoke_shell()
        except paramiko.ssh_exception.AuthenticationException as auth_err:
            err_msg = hostname + str(auth_err)
            msg.append(err_msg)
            continue
        except Exception as err:
            err_msg = hostname + str(err)
            msg.append(err_msg)
            continue
        else:
            if vender == "huawei":
                command.send("display current-configuration" + "\n")
            elif vender == "cisco":
                command.send("enable" + "\n")
                command.send(enable_password + "\n")
                command.send("terminal length 0" + "\n")
                command.send('show running-config' + "\n")

            time.sleep(10)

            conf = command.recv(65535).decode("utf8", "ignore")

            now = datetime.now()

            backup_file_name = \
                "dev_" + hostname + "_" + str(now.year) + str(now.month) + \
                str(now.day) + str(time.strftime("%H%M")) + ".cfg"
            backup_file = backup_dir + backup_file_name
            backup = open(backup_file, "w")
            backup.write(conf)
            backup.close()
            ssh_client.close()
            msg.append(hostname + " backup successful!")

    return "\n".join(msg)
