from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, RawFlowData
import random, json, time

def generate_flow():
    queryset_flow = RawFlowData.objects
    nums = queryset_flow.all().count()
    up = 0
    down = 0
    newnums = random.randint(0, 100)
    for i in range(0, newnums):
        k = random.randint(1, nums + 1)
        new_flow = queryset_flow.get(pk=k)
        up += new_flow.out_flow
        down += new_flow.in_flow
    time_now = time.time()
    return {'up': up, 'down': down, 'time': time_now}


class FlowGenerateView(APIView):
    permission_classes = [AllowAny]

    queryset = Site.objects.all()
    queryset_eq = Equipment.objects.all()
    def get(self, request):
        for i in self.queryset:
            try:
                flow_list = json.loads(i.flow_data)
            except:
                flow_list = []
            if len(flow_list) >= 6:
                del(flow_list[0])
            eqset = self.queryset_eq.filter(site=i.pk)
            site_up = 0
            site_down = 0
            site_time = time.time()
            for j in eqset:
                try:
                    flow_list_eq = json.loads(j.flow_data)
                except:
                    flow_list_eq = []
                if len(flow_list_eq) >= 6:
                    del(flow_list_eq[0])
                new_flow = generate_flow()
                flow_list.append(new_flow)
                j.total_up += new_flow['up']
                j.total_down += new_flow['down']
                site_up += new_flow['up']
                site_down += new_flow['down']
                j.flow_data = json.dumps(flow_list)
            i.total_up += site_up
            i.total_down += site_down
            flow_list.append({'up': site_up, 'down': site_down, 'time': site_time})
        return Response("", 200)
