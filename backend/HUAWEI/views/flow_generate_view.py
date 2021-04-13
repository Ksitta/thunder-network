from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, RawFlowData
import random, json, time

def generate_flow():
    queryset_flow = RawFlowData.objects.all()
    nums = 100000
    up = 0
    down = 0
    newnums = random.randint(0, 100)
    for i in range(0, newnums):
        k = random.randint(1, nums + 1)
        new_flow = queryset_flow.get(pk=k)
        up += new_flow.out_flow
        down += new_flow.in_flow
    return {'up': up, 'down': down}


class FlowGenerateView(APIView):
    permission_classes = [AllowAny]

    queryset_site = Site.objects.all()
    queryset_eq = Equipment.objects.all()
    def get(self, request):
        local_time = time.localtime()
        site_time = str(local_time.tm_year) + '-' + str(local_time.tm_mon) + '-' + str(local_time.tm_mday) + ' ' \
                    + str(local_time.tm_hour) + ':' + str(local_time.tm_min) + ':' + str(local_time.tm_sec)
        for i in self.queryset_site:
            try:
                flow_list = json.loads(i.flow_data)
            except:
                flow_list = []
            if len(flow_list) >= 6:
                del(flow_list[0])
            eqset = self.queryset_eq.filter(site=i.pk)
            site_up = 0
            site_down = 0
            for j in eqset:
                try:
                    flow_list_eq = json.loads(j.flow_data)
                except:
                    flow_list_eq = []
                if len(flow_list_eq) >= 6:
                    del(flow_list_eq[0])
                new_flow = generate_flow()
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
        return Response("", 200)
