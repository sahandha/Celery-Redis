import os

from celery import Celery


app = Celery('tasks', broker='redis://redis-service.redis.svc.cluster.local:6379/0', backend='redis://redis-service.redis.svc.cluster.local:6379/0')

@app.task(name='celery_conf.add', args='(x,y)')
def add(x, y):
    return x + y



@app.task
def subtract(x, y):
    return x - y
