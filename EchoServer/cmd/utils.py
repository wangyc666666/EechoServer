#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wangyc'
# __time__ = 2018/8/13 21:18
# Copyright (c) 2018 ruijie Corp.
# All Rights Reserved.


import fcntl
import json
import os
import copy


def mode_map(mode_type):
    # 服务模式对应关系
    map_dic = {'lower': 0, 'upper': 1, 'normal': 2, 'show': 3}
    if mode_type in map_dic:
        return True
    else:
        return False


def get_data_from_file():
    # 锁住文件并读取文件内容
    with open('/tmp/EchoServerMode', 'r') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        data = f.read()
    return data


def init_data_with_lock():
    # 锁住文件并初始化数据
    data = {'mode_type': {}, 'str_total_n': 0, 'Clients': 0, "default": "upper"}
    data = json.dumps(data)
    with open('/tmp/EchoServerMode', 'w') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(data)


def default_mode_with_lock(mode_t):
    # 锁住文件并设置EchoServer模式
    data = json.loads(get_data_from_file())
    data_n = copy.deepcopy(data)
    for k, v in data_n['mode_type'].items():
        data['mode_type'][k] = mode_t
    data['default'] = mode_t
    data = json.dumps(data)
    with open('/tmp/EchoServerMode', 'w') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(data)


def get_default_mode():
    data = json.loads(get_data_from_file())
    mode_type = data.get('default')
    return mode_type


def update_mode_to_file_with_lock(mode_type, client_id):
    # 锁住文件并设置EchoServer模式
    data = get_data_from_file()
    data = json.loads(data)
    if client_id in data['mode_type']:
        data['mode_type'][client_id] = mode_type
    else:
        data['mode_type'].setdefault(client_id, mode_type)
    data = json.dumps(data)
    with open('/tmp/EchoServerMode', 'w') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(data)


def read_from_file_with_lock(c_id):
    # 锁住文件并读取当前已设置的模式
    data = json.loads(get_data_from_file())
    mode_type = data.get('mode_type').get(str(c_id))

    return mode_type


def update_str_n_with_lock(_str):
    # 锁住文件、统计已处理的字符数，并更新文件
    data = get_data_from_file()
    data = json.loads(data)
    s_total_n = len(_str)
    data['str_total_n'] += s_total_n
    data = json.dumps(data)
    with open('/tmp/EchoServerMode', 'w') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(data)


def show_with_lock():
    # 锁住文件并、查询服务信息
    data = get_data_from_file()
    total_n = json.loads(data).get('str_total_n')
    clients = json.loads(data).get('Clients')
    mode_type = json.loads(data).get('default')
    view_data = '''Server info:
    Global mode: %s
    Characters: %s
    Clients: %s''' % (mode_type, total_n, clients)
    return view_data


def client_cnn_with_lock():
    # 锁住文件、更新客户端连接数
    data = get_data_from_file()
    data = json.loads(data)
    data['Clients'] += 1
    data = json.dumps(data)
    with open('/tmp/EchoServerMode', 'w') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(data)


def client_cnn_reduce_with_lock():
    # 锁住文件、更新客户端连接数
    data = get_data_from_file()
    data = json.loads(data)
    data['Clients'] -= 1
    data = json.dumps(data)
    with open('/tmp/EchoServerMode', 'w') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(data)


def mk_log():
    # 创建程序依赖目录
    path_list = ['/var/log/EchoServer/', '/etc/EchoServer/']
    for path in path_list:
        if not os.path.exists(path):
            os.makedirs(path)
