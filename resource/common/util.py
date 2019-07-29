#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass


class DictToObj():
    """
    将字典转化为对象
    """

    def __init__(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
