#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wangyc'
# __time__ = 2018/8/13 21:18
# Copyright (c) 2018 ruijie Corp.
# All Rights Reserved.


from EchoServer.log.logme import EchoLog
from EchoServer.cmd import server
from EchoServer.config import app
from oslo_log import log as logging
from oslo_config import cfg
from EchoServer.cmd import utils
CONF = cfg.CONF
LOG = logging.getLogger(__name__)


def main():
    # EchoServer 服务端启动
    try:
        # 初始化目录
        utils.mk_log()
        EchoLog().log_file('/etc/EchoServer/EchoServer.conf')
        utils.init_data_with_lock()
        # 载入配置
        app.opts_register_default()
        # 启动服务进程
        ser = server.EchoServer(CONF.ip, CONF.port, CONF.limit)
        ser.start()
        ser.run_forever()
    except Exception as e:
        LOG.error(str(e))


def cli_main():
    try:
        # server 命令行程序入口
        server.my_cli()
    except Exception as e:
        LOG.error(str(e))





