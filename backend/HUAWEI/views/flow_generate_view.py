from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, RawFlowData
import random, json
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


class FlowGenerateView(APIView):
    permission_classes = [AllowAny]

    queryset_site = Site.objects.all()
    queryset_eq = Equipment.objects.all()
    queryset_flow = RawFlowData.objects.all()
    flow_nums = len(queryset_flow)
    def get(self, request):
        self.inner_generate()
        return Response("", 200)

    def inner_generate(self):
        with open('./flow.log', mode='a+') as file:
            file.write(str(time.time()) + " generated flow info\n")
        site_time = datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        for i in self.queryset_site:
            if not i.status == 0:
                continue
            try:
                flow_list = json.loads(i.flow_data)
            except:
                flow_list = []
            if len(flow_list) >= 6:
                del (flow_list[0])
            eq_set = self.queryset_eq.filter(site=i.pk)
            site_up = 0
            site_down = 0
            for j in eq_set:
                if not j.eq_status == 1:
                    continue
                try:
                    flow_list_eq = json.loads(j.flow_data)
                except:
                    flow_list_eq = []
                if len(flow_list_eq) >= 6:
                    del (flow_list_eq[0])
                new_flow = self.generate_flow()
                new_flow['time'] = site_time
                flow_list_eq.append(new_flow)
                j.total_up += new_flow['up']
                j.total_down += new_flow['down']
                site_up += new_flow['up']
                site_down += new_flow['down']
                j.flow_data = json.dumps(flow_list_eq)
                j.save()
            i.total_up += site_up
            i.total_down += site_down
            flow_list.append({'up': site_up, 'down': site_down, 'time': site_time})
            i.flow_data = json.dumps(flow_list)
            i.save()


    def generate_flow(self):
        up = 0
        down = 0
        newnums = random.randint(0, 100)
        for i in range(0, newnums):
            k = random.randint(1, self.flow_nums)
            new_flow = self.queryset_flow.get(pk=k)
            up += new_flow.out_flow
            down += new_flow.in_flow
        return {'up': up, 'down': down}
