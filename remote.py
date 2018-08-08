#!/usr/bin/env python
# -*- coding: utf-8; -*-


from __future__ import print_function
import telnetlib
import sys
import time
import paramiko
import os

def remote_cmd(ip, flag):
    v = None
    retry = 3
    for i in range(0, retry):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for k in range(0, retry):
            try:
                ssh.connect(ip, 22, 'root')
                break
            except:
                ssh.close()
                if k == retry - 1:
                    return None
        try:
            if (int(flag) == 0):
                stdin, stdout, stderr = ssh.exec_command(
                    'cgminer-api estats')
            elif (int(flag) == 1):
                stdin, stdout, stderr = ssh.exec_command(
                    'cgminer-api edevs')
            elif (int(flag) == 2):
                stdin, stdout, stderr = ssh.exec_command(
                    'cgminer-api summary')
            elif (int(flag) == 3):
                stdin, stdout, stderr = ssh.exec_command(
                    'cgminer-api debug\|D')
            elif (int(flag) == 4):
                stdin, stdout, stderr = ssh.exec_command(
                    '/etc/init.d/cgminer restart')
            else:
                return None

            time.sleep(2)
            v = stdout.read()
        except:
            ssh.close()
            continue

        ssh.close()
        break
    return v

def remote_scp(ip, flag):
    if (int(flag) == 0):
        os.system("scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@%s:/etc/config/cgminer ./result-%s" % (ip, ip))
    elif (int(flag) == 1):
        os.system("scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ./result-%s/cgminer root@%s:/etc/config/" % (ip, ip))
    else:
        print("ip = %s, flag = %s" % (ip, flag))
        return False

    return True
