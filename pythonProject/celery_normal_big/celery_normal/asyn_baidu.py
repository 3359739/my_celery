import time
from random import random

from celery_normal_big.celery_normal.celery import app


@app.task
def baidu():
    print("开始爬取百度")
    time.sleep(3)
    print("爬取完成")
    return f"{random}"


@app.task
def baidu_delay():
    print("开始爬取百度delay")
    time.sleep(3)
    print("爬取完成delay")
    return f"{random}"

