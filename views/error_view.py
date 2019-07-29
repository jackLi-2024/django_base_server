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

from rest_framework.views import APIView
from views.tasks import add
from resource.common import output
from resource.extension.log import logging
from resource.common.catch_exception import catch_exception


class ErrorView(APIView):
    """
    错误路由视图
        对路由异常捕获处理
    """

    @catch_exception
    def get(self, request, *args, **kwargs):
        return output.ErrorResponse(msg="Please give correct path", status=500)

    @catch_exception
    def post(self, request, *args, **kwargs):
        return output.ErrorResponse(msg="Please give correct path", status=500)
