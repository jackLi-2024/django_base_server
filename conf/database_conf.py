import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

databases = {

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',  # 数据库引擎 Django需要mysqlclient 1.3.13或更高版本。
    #     'NAME': 'test',  # 你要存储数据的库名，事先要创建之
    #     'USER': 'root',  # 数据库用户名
    #     'PASSWORD': '123456',  # 密码
    #     'HOST': '192.168.1.2',  # 主机
    #     'PORT': '3307',  # 数据库使用的端口
    #     'OPTIONS': {  # 取消外键检查 否则删除带外键字段的记录会报错
    #         "init_command": "SET foreign_key_checks = 0;",
    #     }
    #
    # },
    # 'oracle': {
    #     'ENGINE': 'django.db.backends.oracle',#cx_Oracle  需要安装
    #     'NAME': 'ORCL',
    #     'USER': 'devcq',
    #     'PASSWORD': 'baIaGbnx9C',
    #     'HOST': '116.62.196.190',
    #     'PORT': '1521',
    #     'OPTIONS': {
    #         'threaded': True,
    #     }
    # },
    #
    #  'Postgresql': {
    #
    #      'ENGINE': 'django.db.backends.postgresql_psycopg2',#需要pip install psycopg2
    #      'NAME': 'testdb',  # 数据库名字(需要先创建)
    #      'USER': 'postgres',  # 登录用户名
    #      'PASSWORD': '123456',  # 密码
    #      'HOST': '',  # 数据库IP地址,留空默认为localhost
    #      'PORT': '5432',  # 端口
    #
    #     },
    # 'sqlite': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

}