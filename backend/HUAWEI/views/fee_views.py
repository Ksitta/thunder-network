from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, FlowData
from HUAWEI.serializers import SiteFlowSerializer, EquipmentFlowSerializer, FlowDataSerializer
from rest_framework.permissions import IsAuthenticated
from copy import copy
import time
from datetime import datetime
import pytz

beijing = pytz.timezone("Asia/Shanghai")

def trans_cacul(a: int):
    if a == 1:
        return 0.8
    else:
        return 0.7

def trans_time(timestamp):
    utc_date = datetime.utcfromtimestamp(timestamp)
    fmt = '%Y-%m-%d %H:%M:%S'
    utc = pytz.utc
    utc_loc_time = utc.localize(utc_date)
    return utc_loc_time.astimezone(beijing).strftime(fmt)


class FeeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        return_data = {}
        time_now = int(time.time())
        to_time_last = time_now - (time_now % 14400)
        from_time_last = to_time_last - 86400
        try:
            to_time = int(request.GET.get('to_time'))
            from_time = int(request.GET.get('from_time'))
        except:
            time_now = int(time.time())
            to_time = time_now - (time_now % 14400)
            from_time = to_time - 86400

        from_time = min(from_time, from_time_last)
        to_time = min(to_time_last, to_time)
        if user.user_type == 1 or user.user_type == 2:  # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=user)
        div = (to_time - from_time) / 6
        sites_fee = []
        total_fee = 0
        for thesite in sites:
            site_serializer = SiteFlowSerializer(instance=thesite)
            eqs_info = Equipment.objects.filter(site=thesite.pk)
            thesite_fee = copy(site_serializer.data)
            factor = trans_cacul(thesite.billing_level)
            site_flow_data = []
            site_total = 0
            site_view_counts = 0
            for i in range(0, 6):
                single = {'fee': 0, 'time': trans_time(from_time + (i + 1) * div),
                          'start_time': trans_time(from_time + i * div)}
                site_flow_data.append(single)
            for eq in eqs_info:
                flow_data = []
                all_data = FlowData.objects.filter(eq=eq, generate_time__gte=from_time, generate_time__lte=to_time)
                serializers = FlowDataSerializer(instance=all_data, many=True)
                for i in range(1, 7):
                    single = {'fee': 0, 'time': trans_time(from_time + (i + 1) * div)}
                    flow_data.append(single)
                for flow in serializers.data:
                    k = int((flow['generate_time'] - from_time) / (div + 1))
                    site_flow_data[k]['fee'] += flow['in_flow'] + flow['out_flow']
                    site_total += flow['out_flow'] + flow['in_flow']
                    site_view_counts += 1
            site_total = site_total * factor / 1024 / 1024 / 1024
            thesite_fee['total_fee'] = site_total
            thesite_fee['rate_unit'] = "GB/元"
            total_fee += site_total
            if thesite.billing_level == 1:
                total_fee += (to_time - from_time) / 2626560 * 10
            else:
                total_fee += (to_time - from_time) / 365 / 86400 * 50
            sites_fee.append(thesite_fee)
        return_data['sites_fee'] = sites_fee
        return_data['total_fee'] = total_fee
        return Response(return_data, status=status.HTTP_200_OK)

