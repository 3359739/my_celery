from celery import Celery
from celery.schedules import schedule

redis_url1 = 'redis://127.0.0.1:6379/1'
redis_url2 = 'redis://127.0.0.1:6379/2'
app=Celery("celery_normal",broker=redis_url1,backend=redis_url2,include=['celery_normal.asyn_baidu'])


app.conf.timezone='Asia/Shanghai'
app.conf.beat_schedule={
    'send_email': {
        'task': 'celery_normal.asyn_baidu.baidu',
        "schedule":1,
        "args":()
    }
}