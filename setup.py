#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wangyc'
# __time__ = 2018/8/10 20:18
# Copyright (c) 2018 ruijie Corp.
# All Rights Reserved.


from setuptools import setup, find_packages


setup(
    name="EchoServer",
    version="1.0.0",
    author="wangyc",
    author_email="wangyongcheng@ruijie.com.cn",
    description="End-to-end communication",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'server = EchoServer.cmd.main:cli_main',
            'EchoServer = EchoServer.cmd.main:main',
            'client = EchoServer.cmd.client:echo_client',
        ],
        'oslo.config.opts': [
            'EchoServerCfg = EchoServer.config.app:list_opts'
        ]

    }
)
