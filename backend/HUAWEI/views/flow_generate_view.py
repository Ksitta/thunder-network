from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, RawFlowData, FlowData
import random, json
import time
try:
    from config.local_settings import interval_time
except:
    interval_time = 3600
import pytz

from apscheduler.schedulers.background import BackgroundScheduler
from .task import flow_info

scheduler = BackgroundScheduler()
scheduler.add_job(flow_info, 'interval', seconds=interval_time)
with open('./log.txt', mode='a+') as file:
    file.write("successfully added task\n")
print("successfully added task\n")
scheduler.start()

beijing = pytz.timezone("Asia/Shanghai")


class FlowGenerateView(APIView):
    permission_classes = [AllowAny]

    queryset_site = Site.objects.all()
    queryset_eq = Equipment.objects.all()
    queryset_flow = RawFlowData.objects.all()
    flow_nums = len(queryset_flow)
    create_list = []

    def get(self, request):
        self.inner_generate()
        return Response("", 200)

    def inner_generate(self):
        with open('./flow.log', mode='a+') as file:
            file.write(str(time.time()) + " generated flow info\n")
        now_time = time.time()
        self.create_list.clear()
        for site in self.queryset_site:
            if not site.status == 0:
                continue
            eq_set = self.queryset_eq.filter(site=site.pk)
            for eq in eq_set:
                if not eq.eq_status == 1:
                    continue
                self.generate_flow(site.user, site, eq, now_time)
        FlowData.objects.bulk_create(self.create_list)
        self.create_list.clear()

    def generate_flow(self, user, site, eq, now_time):
        new_nums = random.randint(0, 100)
        for i in range(0, new_nums):
            k = random.randint(1, self.flow_nums)
            raw_flow = self.queryset_flow.get(pk=k)
            new_flow = FlowData(dest_ip=raw_flow.dest_ip, source_ip=raw_flow.source_ip,
                                out_flow=raw_flow.out_flow, in_flow=raw_flow.in_flow,
                                site=site, user=user, eq=eq, generate_time=now_time)
            self.create_list.append(new_flow)
