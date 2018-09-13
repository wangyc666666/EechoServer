#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wangyc'
# __time__ = 2018/8/13 21:18
# Copyright (c) 2018 ruijie Corp.
# All Rights Reserved.


from oslo_config import cfg

defaultOpts = [
    cfg.StrOpt('ip', default='0.0.0.0', help="""
    log_config_append is set. (string ip)
    """),
    cfg.IntOpt('port', default='8888', help="""
    port set
    """),
    cfg.IntOpt('limit', default='8', help="""
    limit  set
    """),
]

sysCfgOpts = [
    cfg.BoolOpt('debug', default=False, help=""" 
    Whether to run the debug the default Fasle.
    """),
    cfg.StrOpt('log_file', default='EchoServer.log', help="""
    log_config_append is set. (string value)
    """),
    cfg.StrOpt('log_dir', default='/var/log/EchoServer', help="""
    is ignored if log_config_append is set. (string value)
    """),
    cfg.BoolOpt('use_stderr', default=False, help="""
    # Log output to standard error. This option is ignored if log_config_append is
    # set. (boolean value)
    """),
]


def opts_register_default():
    cfg.CONF.register_opts(defaultOpts)


def list_opts():
    # Automatic generation of configuration files
    # Allows the generation of the help text for
    # the baz_group OptGroup object. No help
    # text is generated for the 'blaa' group.
    return [('DEFAULT', sysCfgOpts + defaultOpts)]

