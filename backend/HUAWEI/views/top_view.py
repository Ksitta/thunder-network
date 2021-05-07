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

class TopSiteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        try:
            to_time = int(request.GET.get('to_time'))
            from_time = int(request.GET.get('from_time'))
        except:
            to_time = time.time()
            from_time = to_time - 86400
        if user.user_type == 1 or user.user_type == 2:  # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=user)

        sites_flow = []
        # 各个站点总流量统计
        for thesite in sites:
            site_serializer = SiteFlowSerializer(instance=thesite)
            eqs_info = Equipment.objects.filter(site=thesite.pk)
            thesite_flow = copy(site_serializer.data)
            site_total = 0
            for eq in eqs_info:
                all_data = FlowData.objects.filter(eq=eq, generate_time__gte=from_time, generate_time__lte=to_time)
                serializers = FlowDataSerializer(instance=all_data, many=True)
                for flow in serializers.data:
                    site_total += flow['out_flow']
                    site_total += flow['in_flow']

            thesite_flow['total'] = site_total

            sites_flow.append(thesite_flow)
        li = sorted(sites_flow, key=lambda x: x['total'], reverse=True)
        li = li[:5:]
        return Response(li, status=status.HTTP_200_OK)