#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wangyc'
# __time__ = 2018/8/13 21:18
# Copyright (c) 2018 ruijie Corp.
# All Rights Reserved.


from threading import Thread
import socketserver
from EchoServer.cmd import utils
import time
from oslo_log import log as logging
from oslo_config import cfg
CONF = cfg.CONF
LOG = logging.getLogger(__name__)
client_id = 0


class MyServer(socketserver.BaseRequestHandler):
    # socket 服务通信主要程序
    def handle(self):
        global client_id
        client_id += 1
        conn = self.request
        conn.sendall(bytes("Client ID is " + str(client_id) + ' .', encoding='utf8'))
        utils.client_cnn_with_lock()
        get_default_mode = utils.get_default_mode()
        utils.update_mode_to_file_with_lock(get_default_mode, client_id)
        LOG.debug('A new connect.')
        while True:
            data = self.request.recv(1024).decode(encoding='utf8')
            if ':' in data:
                c_id = int(data.split(':', -1)[0])
            else:
                break
            data = data.split(':', -1)[-1]
            if len(data) == 0:
                break

            if data == 'quit' or data == 'exit':
                utils.client_cnn_reduce_with_lock()
                print('Disconnected from the client %s!' % (c_id))
                break
            LOG.info("[%s] says:%s" % (self.client_address, data))
            utils.update_str_n_with_lock(data)
            time.sleep(0.2)
            server_mode = utils.read_from_file_with_lock(c_id)
            data = bytes(data, encoding="utf-8")
            if server_mode == 'lower':
                self.request.sendall(data.lower())
            elif server_mode == 'upper':
                self.request.sendall(data.upper())
            elif server_mode == 'normal':
                self.request.sendall(data)
            else:
                self.request.sendall(data.upper())


class EchoServer(object):
    def __init__(self, ip, port, limit):
        self.ip = ip
        self.port = port
        self.limit = limit
        self.server = socketserver.TCPServer((self.ip, self.port), MyServer)

    def start(self):
        # 限制客户端连接数量
        for n in range(self.limit):
            t = Thread(target=self.server.serve_forever)
            t.daemon = True
            t.start()

    def run_forever(self):
        # 永久监听
        self.server.serve_forever()


def my_cli():
    # server 命令行程序
    while True:
        try:
            mode_type = input("Server>>").strip()
            if mode_type == 'quit'or mode_type == 'exit':
                exit(0)
            # 获取设置模式
            mode_t = mode_type.split(' ', -1)[-1]
            # 查看关键字是否存在
            if not utils.mode_map(mode_t):
                continue
            if mode_t == 'show':
                data = utils.show_with_lock()
                print(data)
            # 获取客户端id
            mode_id = mode_type.split(' ', -1)[1]
            if mode_id == '0':
                # 设置为0时，为全局配置，对所有用户生效
                utils.default_mode_with_lock(mode_t)
                continue
            else:
                # 确认是否有此用户id
                user_id = utils.read_from_file_with_lock(mode_id)
                if user_id:
                    utils.update_mode_to_file_with_lock(mode_t, mode_id)
                else:
                    continue
        except Exception:
            continue

