# Celery
用Celery在flask/django里实现异步任务，发送短信邮件等
## 使用说明
### 安装使用Celery
* pip install -U Celery
* 创建实例
```python
from celery import Celery
# 创建 celery 实例
celery_app = Celery('demo')
```
* 加载Celery配置
```python
# 指定消息队列的位置, 使用方式:
# rabbitmq 用法配置:
broker_url= 'amqp://用户名:密码@ip地址:5672'
# 例如: 
# demoname: 在rabbitq中创建的用户名, 注意: 远端链接时不能使用guest账户.
# 123456: 在rabbitq中用户名对应的密码
# ip部分: 指的是当前rabbitq所在的电脑ip
# 5672: 是规定的端口号
broker_url = 'amqp://demoname:123456@172.16.238.128:5672'
# 用redis做消息队列
# redis 用法配置:
broker_url='redis://127.0.0.1:6379/3
```
* main.py文件配置
```python
# 导入 Celery 类
from celery import Celery

# 创建 celery 对象
# 需要添加一个参数,是个字符串, 内容随意添加
celery_app = Celery('demo')

# 给 celery 添加配置
# 里面的参数为我们创建的 config 配置文件:
celery_app.config_from_object('celery_tasks.config')

# 让 celery_app 自动捕获目标地址下的任务,注册
celery_app.autodiscover_tasks(['celery_tasks.sms'])
```
* 定义发送任务
```python
# bind：保证task对象会作为第一个参数自动传入
# name：异步任务别名
# retry_backoff：异常自动重试的时间间隔 第n次(retry_backoff×2^(n-1))s
# max_retries：异常自动重试次数的上限
@celery_app.task(bind=True, name='ccp_send_sms_code', retry_backoff=3)
def ccp_send_sms_code(self, mobile, sms_code):
    """
    发送短信异步任务
    :param mobile: 手机号
    :param sms_code: 短信验证码
    :return: 成功0 或 失败-1
    """

    try:
        # 调用 CCP() 发送短信, 并传递相关参数: 
        result = CCP().send_template_sms(mobile, 
                                         [sms_code, 5], 
                                         1)

    except Exception as e:
        # 如果发送过程出错, 打印错误日志
        logger.error(e)

        # 有异常自动重试三次
        raise self.retry(exc=e, max_retries=3)

       # 如果发送成功, rend_ret 为 0: 
    if result != 0:
        # 有异常自动重试三次
        raise self.retry(exc=Exception('发送短信失败'), max_retries=3)

    return result
```
* 启动服务
```python
celery -A celery_tasks.main worker -l info
```
* 调用发送任务
```python# 
# Celery 异步发送短信验证码
ccp_send_sms_code.delay(mobile, sms_code)

# Celery 异步发送邮件
send_verify_email.delay(email,verify_url)
```
    
    
