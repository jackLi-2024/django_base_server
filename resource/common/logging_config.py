import os
from conf import log_conf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_LOG_DIR = os.path.join(BASE_DIR, "../log")
if not os.path.isdir(BASE_LOG_DIR):
    os.mkdir(BASE_LOG_DIR)

logs = {
    'version': 1,
    'disable_existing_loggers': False,
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        # 简单的日志格式
        'simple': {
            'format': '%(levelname)s %(module)s %(asctime)s %(message)s'
        },
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 在终端打印
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        # 专门用来记错误日志
        'error': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, log_conf.filename),  # 日志文件
            'maxBytes': log_conf.maxBytes,  # 日志大小 50M
            'backupCount': log_conf.backupCount,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'tf_handlers': {
            'level': 'DEBUG',
            # 若日志超过指定文件的大小，会再生成一个新的日志文件保存日志信息
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when':log_conf.when,
            'interval' : log_conf.interval,
            'backupCount':log_conf.backupCount,
            # 文件地址
            'filename': os.path.join(BASE_LOG_DIR,log_conf.filename),
            # 指定保存格式
            'formatter': 'simple'
                }
    },
    'loggers': {
        '': {
            'handlers': ['console'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        'error': {
            'handlers': ['error'],
            'level': 'INFO',
        },
        'tf': {
            'handlers': ['tf_handlers'],
            'level': 'INFO'
        }
    },
}