# 任务队列的链接地址
broker_url = 'redis://127.0.0.1:6379/15'
# 结果队列的链接地址
result_backend = 'redis://127.0.0.1:6379/14'
# 时区设置
timezone = 'Asia/Shanghai'

# 使用定时任务必须确保设置了时区
from .main import app
from celery.schedules import crontab
app.conf.beat_schedule = {
    'check-order': {
        'task': 'check_order',  # 定时执行的任务
        'schedule': 30.0,       # 定时执行的频率，表示每30秒执行一次
        # 'schedule': crontab(minute="*/5"),  # 定时执行的频率，
        # 'args': (16, 16)        # 定时的任务参数
    }
}

