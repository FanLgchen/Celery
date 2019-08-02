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
