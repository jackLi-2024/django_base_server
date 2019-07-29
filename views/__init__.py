from __future__ import absolute_import, unicode_literals
# 确保应用程序总是能被找到
# Django启动，shared_task将使用这个应用程序。
from controller.celery import app as celery_app

__all__ = ['celery_app']