from apscheduler.schedulers.background import BackgroundScheduler
from django.test.client import Client
from django.urls import reverse
from HUAWEI.models import Site, Equipment, RawFlowData, FlowData
import time, random


def generate_flow(user, site, eq, now_time, create_list, queryset_flow, flow_nums):
    new_nums = random.randint(0, 100)
    for i in range(0, new_nums):
        k = random.randint(1, flow_nums)
        raw_flow = queryset_flow.get(pk=k)
        new_flow = FlowData(dest_ip=raw_flow.dest_ip, source_ip=raw_flow.source_ip,
                            out_flow=raw_flow.out_flow, in_flow=raw_flow.in_flow,
                            site=site, user=user, eq=eq, generate_time=now_time)
        create_list.append(new_flow)

def flow_info():
    queryset_site = Site.objects.all()
    queryset_flow = RawFlowData.objects.all()
    queryset_eq = Equipment.objects.all()
    flow_nums = len(queryset_flow)
    print('succ')
    with open('./flow.log', mode='a+') as file:
        file.write(str(time.time()) + " generated flow info\n")
    now_time = time.time()
    create_list = []
    for site in queryset_site:
        if not site.status == 0:
            continue
        eq_set = queryset_eq.filter(site=site.pk)
        for eq in eq_set:
            if not eq.eq_status == 1:
                continue
            generate_flow(site.user, site, eq, now_time, create_list, queryset_flow, flow_nums)
    FlowData.objects.bulk_create(create_list)

