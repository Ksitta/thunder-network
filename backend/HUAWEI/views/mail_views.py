from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from HUAWEI.models import User, Site, FlowData
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import time
from datetime import datetime
import pytz

beijing = pytz.timezone("Asia/Shanghai")

def trans_time(timestamp):
    utc_date = datetime.utcfromtimestamp(timestamp)
    fmt = '%Y-%m-%d'
    utc = pytz.utc
    utc_loc_time = utc.localize(utc_date)
    return utc_loc_time.astimezone(beijing).strftime(fmt)

def trans_cacul(a:int):
    if a == 1:
        return 0.8
    else:
        return 0.7

def send_email(user_name, email_address, mory):
    if mory == 1:
        time_dec = 2626560
        time_p = '月度'
    else:
        time_dec = 31536000
        time_p = '年度'
    from_email = "thunder_network@126.com"
    user = User.objects.get(username=user_name)
    start_time = int(time.time()) - time_dec
    site = Site.objects.filter(user=user.pk)
    flow_list = []
    total_flow = 0
    total_money_num = 0.0
    month = 0
    year = 0
    time_now = time.time()
    for i in site:
        site_flow = FlowData.objects.filter(site=i, generate_time__gte=start_time)
        one_site_flow = 0
        for each in site_flow:
            one_site_flow += each.in_flow + each.out_flow
        one_site_flow /= (1024 * 1024 * 1024)
        total_flow += one_site_flow
        site_money = one_site_flow * trans_cacul(i.billing_level)
        flow_list.append({'site_name': i.site_name, 'site_flow': '%.2f' % one_site_flow,
                          'site_money': '%.2f' % site_money})
        total_money_num += site_money
        if i.billing_level == 1:
            month += 1
            if mory == 2:
                month + (time_now - i.create_time.timestamp()) / 2626560
        else:
            year += 1
    if mory == 1:
        flow_list.append({'site_name': '基础月费(不包含年费订单)', 'site_money': month * 10})
    else:
        flow_list.append({'site_name': '基础月费(包含年费和月费)', 'site_money': month * 10 + year * 50})
    total_money_num += month * 10 + year * 50
    total_money = '%.2f' % total_money_num
    if email_address:
        to_list = [
            email_address
        ]
    else:
        to_list = [
            user.contact_email
        ]
    mail_data = {'flow_list': flow_list, 'total_flow': total_flow, 'total_money': total_money, 'username': user_name,
                 'date': trans_time(int(time.time()))}
    html_body = render_to_string('mail.html', mail_data)

    text_content = ''  # 对方不支持多媒体邮件的话显示这里的内容
    subject = '您本'+time_p+'的账单，请您查收 Thunder-network'  # 邮件标题
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_list)
    # 邮件显示html_body的内容，html编码
    msg.attach_alternative(html_body, "text/html")
    msg.send()

class MailSendView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            email_address = data['email']
            username = data["username"]
        except:
            email_address = None
            username = self.request.user
        send_email(username, email_address, data['mory'])
        return Response("Success", 200)
