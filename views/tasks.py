#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================

descripition: add celery task
"""

from celery import shared_task
import time


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y
