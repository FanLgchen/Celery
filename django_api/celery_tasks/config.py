


# 指定消息队列的位置, 使用方式:
# rabbitmq 用法配置:
# broker_url= 'amqp://用户名:密码@ip地址:5672'

# 例如:
# denoname: 在rabbitq中创建的用户名, 注意: 远端链接时不能使用guest账户.
# 123456: 在rabbitq中用户名对应的密码
# ip部分: 指的是当前rabbitq所在的电脑ip
# 5672: 是规定的端口号
# broker_url = 'amqp://demoname:123456@172.16.238.128:5672'



# redis 用法配置:
broker_url='redis://127.0.0.1:6379/3'