#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
自定义异常类，可自行添加
"""


class DatabaseError(Exception):
    def __init__(self, err='数据库连接异常',Reason=None):
        Exception.__init__(self, err, Reason)


class ReadConfigError(Exception):
    def __init__(self, err='Config读取初始化失败',Reason=None):
        Exception.__init__(self, err, Reason)



