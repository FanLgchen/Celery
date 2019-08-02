
"""发送验证码是另外服务器，用异步处理，不影响主进程"""

"""将代码放在需要发送邮件或短信的文件里"""
#调用封装函数发送短信验证码
ccp_send_sms_code.delay(mobile,sms_code)

#调用封装函数发送邮件
send_verify_email.delay(email,verify_url)

