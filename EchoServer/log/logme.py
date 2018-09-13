#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wangyc'
# __time__ = 2018/8/13 21:18
# Copyright (c) 2018 ruijie Corp.
# All Rights Reserved.


from oslo_log import log as logging
from oslo_config import cfg


class EchoLog(object):
    # 配置文件载入

    def __init__(self):
        self.CONF = cfg.CONF

    def log_file(self, file_dir):
        logging.register_options(self.CONF)
        self.CONF(default_config_files=[file_dir])
        logging.setup(self.CONF, __name__)

    def init_log(self):
        logging.register_options(self.CONF)
        logging.setup(self.CONF, __name__)
