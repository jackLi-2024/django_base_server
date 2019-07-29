BROKER_URL = 'redis://localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://localhost'
CELERY_TASK_SERIALIZER = 'json'

CELERY_TASK_RESULT_EXPIRES = 3600  # celery任务执行结果的超时时间，
# CELERYD_CONCURRENCY = 50  # celery worker的并发数