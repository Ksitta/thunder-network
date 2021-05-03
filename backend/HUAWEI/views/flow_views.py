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


def trans_time(timestamp):
    utc_date = datetime.utcfromtimestamp(timestamp)
    fmt = '%Y-%m-%d %H:%M:%S'
    utc = pytz.utc
    utc_loc_time = utc.localize(utc_date)
    return utc_loc_time.astimezone(beijing).strftime(fmt)


class TotalFlowView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user

        return_data = {'rate_unit': 'byte'}
        total_up = 0
        total_down = 0
        flow_data = []
        try:
            to_time = int(request.GET.get('to_time'))
            from_time = int(request.GET.get('from_time'))
        except:
            to_time = time.time()
            from_time = to_time - 86400
        all_data = FlowData.objects.filter(generate_time__gte=from_time, generate_time__lte=to_time)
        if user.user_type == 1 or user.user_type == 2:  # 运营&网络工程师
            sites = Site.objects.all()
            pass
        else:
            sites = Site.objects.filter(user=user)
            all_data = FlowData.objects.filter(user=user, generate_time__gte=from_time, generate_time__lte=to_time)
        serializers = FlowDataSerializer(instance=all_data, many=True)
        div = (to_time - from_time) / 6
        for i in range(0, 6):
            single = {'up': 0, 'down': 0, 'time': trans_time(from_time + (i + 1) * div)}
            flow_data.append(single)
        for flow in serializers.data:
            k = int((flow['generate_time'] - from_time) / div)
            flow_data[k]['down'] += flow['in_flow']
            flow_data[k]['up'] += flow['out_flow']
            total_up += flow['out_flow']
            total_down += flow['in_flow']

        return_data['total_up'] = total_up
        return_data['total_down'] = total_down
        return_data['flow_data'] = flow_data

        sites_flow = []
        # 各个站点总流量统计
        for thesite in sites:
            site_serializer = SiteFlowSerializer(instance=thesite)
            eqs_info = Equipment.objects.filter(site=thesite.pk)
            thesite_flow = copy(site_serializer.data)

            site_flow_data = []
            site_total_up = 0
            site_total_down = 0
            for i in range(0, 6):
                single = {'up': 0, 'down': 0, 'time': trans_time(from_time + (i + 1) * div),
                          'start_time': trans_time(from_time + i * div)}
                site_flow_data.append(single)
            for eq in eqs_info:
                flow_data = []
                all_data = FlowData.objects.filter(eq=eq, generate_time__gte=from_time, generate_time__lte=to_time)
                serializers = FlowDataSerializer(instance=all_data, many=True)
                for i in range(1, 7):
                    single = {'up': 0, 'down': 0, 'time': trans_time(from_time + (i + 1) * div)}
                    flow_data.append(single)
                for flow in serializers.data:
                    k = int((flow['generate_time'] - from_time) / div)
                    site_flow_data[k]['down'] += flow['in_flow']
                    site_flow_data[k]['up'] += flow['out_flow']
                    site_total_up += flow['out_flow']
                    site_total_down += flow['in_flow']

            thesite_flow['total_up'] = site_total_up
            thesite_flow['total_down'] = site_total_down
            # thesite_flow['flow_data'] = site_flow_data

            sites_flow.append(thesite_flow)

        return_data['sites_flow'] = sites_flow

        return Response(return_data, status=status.HTTP_200_OK)


class SiteFlowView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = self.request.user
        if user.user_type == 1 or user.user_type == 2:  # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=user)
        thesite = sites[int(pk)]

        if thesite.status == 1 or thesite.status == 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        eqs_info = Equipment.objects.filter(site=thesite.pk)

        return_data = {
            'site_flow': {},
            'eq_flows': []
        }

        site_serializer = SiteFlowSerializer(instance=thesite)
        site_flow = copy(site_serializer.data)
        return_data['site_flow'] = site_flow
        eq_flows = []
        try:
            to_time = int(request.GET.get('to_time'))
            from_time = int(request.GET.get('from_time'))
        except:
            to_time = time.time()
            from_time = to_time - 86400
        div = (to_time - from_time) / 6
        site_flow_data = []
        site_total_up = 0
        site_total_down = 0
        for i in range(0, 6):
            single = {'up': 0, 'down': 0, 'time': trans_time(from_time + (i + 1) * div),
                      'start_time': trans_time(from_time + i * div)}
            site_flow_data.append(single)
        for eq in eqs_info:
            eq_data = {"eq_name": eq.eq_name, "rate_unit": "byte"}
            total_up = 0
            total_down = 0
            flow_data = []
            all_data = FlowData.objects.filter(eq=eq, generate_time__gte=from_time, generate_time__lte=to_time)
            serializers = FlowDataSerializer(instance=all_data, many=True)
            for i in range(1, 7):
                single = {'up': 0, 'down': 0, 'time': trans_time(from_time + (i + 1) * div)}
                flow_data.append(single)
            for flow in serializers.data:
                k = int((flow['generate_time'] - from_time) / div)
                flow_data[k]['down'] += flow['in_flow']
                flow_data[k]['up'] += flow['out_flow']
                total_up += flow['out_flow']
                total_down += flow['in_flow']
                site_flow_data[k]['down'] += flow['in_flow']
                site_flow_data[k]['up'] += flow['out_flow']
                site_total_up += flow['out_flow']
                site_total_down += flow['in_flow']
            eq_data['total_up'] = total_up
            eq_data['total_down'] = total_down
            eq_data['flow_data'] = flow_data
            eq_flows.append(eq_data)

        return_data['eq_flows'] = eq_flows
        site_flow['total_up'] = site_total_up
        site_flow['total_down'] = site_total_down
        site_flow['flow_data'] = site_flow_data
        return Response(return_data, status=status.HTTP_200_OK)
