#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wangyc'
# __time__ = 2018/8/13 21:18
# Copyright (c) 2018 ruijie Corp.
# All Rights Reserved.


import socket
import sys

my_id = 0


class SocketClient(object):
    def __init__(self, ip, port):
        global my_id
        self.s = socket.socket()
        self.s.connect((ip, port))
        welcome_msg = self.s.recv(1024).decode(encoding='utf8')
        my_id = welcome_msg.split(' ', -1)[-2]
        print(welcome_msg)

    def close(self):
        self.s.close()

    def send_msg(self):
        global my_id
        while True:
            send_data = input("CLIENT>").strip()
            send_data = my_id + ':' + send_data
            if 'exit' in send_data or 'quit' in send_data :
                self.s.send(bytes(send_data, encoding="utf-8"))
                print('Disconnected from the server！')
                exit(0)
            if len(send_data) == 0:
                continue
            self.s.send(bytes(send_data, encoding="utf-8"))
            recv_data = self.s.recv(1024).decode(encoding='utf8')
            print('ECHO:', recv_data)


def echo_client():
    try:
        try:
            _arg = sys.argv[1]
        except IndexError:
            print('''Usage:
        -u  run in user mode 
        -k  run in kernel mode
                       ''')
            exit()

        if _arg == '-u':
            c = SocketClient('127.0.0.1', 8888)
            c.send_msg()
            c.close()
        elif _arg == '-k':
            c = SocketClient('127.0.0.1', 8888)
            c.send_msg()
            c.close()
        else:
            print('''Usage:         
        -u  run in user mode 
        -k  run in kernel mode
                       ''')
            exit()

    except Exception:
        print('Unable to establish a connection with the server！')
