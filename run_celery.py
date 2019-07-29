#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
启动celery服务测试
"""
import os

if __name__ == '__main__':
    os.system("celery -A controller worker -l info -P eventlet")
