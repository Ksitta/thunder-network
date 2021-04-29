from django.core.mail import send_mail
# send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
send_mail('Subject here', 'Here is the message.', 'thunder_network@126.com',
    ['zhang-qh19@mails.tsinghua.edu.cn'], fail_silently=False)