from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from HUAWEI.models import User, Site, FlowData
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import time


def send_email(user_name, email_address):
    from_email = "thunder_network@126.com"
    user = User.objects.get(username=user_name)
    start_time = int(time.time()) - 2626560
    site = Site.objects.filter(user=user.pk)
    flow_list = []
    total_flow = 0
    for i in site:
        site_flow = FlowData.objects.filter(site=i, generate_time__gte=start_time)
        one_site_flow = 0
        for each in site_flow:
            one_site_flow += each.in_flow + each.out_flow
        one_site_flow /= (1024 * 1024 * 1024)
        total_flow += one_site_flow
        flow_list.append({'site_name': i.site_name, 'site_flow': one_site_flow, 'site_money': one_site_flow * 0.8})
    total_money = total_flow * 0.8
    if(email_address):
        to_list = [
            email_address
        ]
    else:
        to_list = [
            user.contact_email
        ]
    mail_data = {'flow_list': flow_list, 'total_flow': total_flow, 'total_money': total_money}
    html_body = render_to_string('mail.html', mail_data)

    text_content = ''  # 对方不支持多媒体邮件的话显示这里的内容
    subject = '您的本月账单，请您查收 Thunder-network'  # 邮件标题
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
        except:
            email_address = None
        send_email(data["username"], email_address)
        return Response("Success", 200)
