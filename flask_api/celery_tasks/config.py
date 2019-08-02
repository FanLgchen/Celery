class CeleryConfig(object):
    """
    Celery默认配置
    """
    broker_url = 'amqp://python:rabbitmqpwd@localhost:5672/demo'

    task_routes = {
        'sms.*': {'queue': 'sms'},
    }

    # 阿里短信服务
    DYSMS_ACCESS_KEY_ID = ''
    DYSMS_ACCESS_KEY_SECRET = ''