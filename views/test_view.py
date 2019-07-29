#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
description: 该视图为测试视图，定义了接口类API的模块与规范
    主要介绍
            日志模块的导入渝使用
            标准输出模块的导入与使用
            捕获异常的通用函数
            字典参数转对象处理
"""

from rest_framework.views import APIView
from views.tasks import add
from resource.common import output
from resource.common.util import DictToObj
from resource.extension.log import logging
from resource.common.catch_exception import catch_exception


class Test(APIView):
    """
    测试代码：

    """

    @catch_exception
    def get(self, request, *args, **kwargs):
        params = DictToObj(request.params)
        r = add.delay(4, 12)
        result = r.wait()
        logging.info("ok!")
        if not result:
            return output.ErrorResponse(msg="fail,no result", status=500)
        return output.NormalResponse({'detail': result}, status=200)
