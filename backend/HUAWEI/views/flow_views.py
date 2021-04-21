from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment
from HUAWEI.serializers import SiteFlowSerializer, EquipmentFlowSerializer
from rest_framework.permissions import IsAuthenticated
from copy import copy
import json

class TotalFlowView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        if user.user_type == 1 or user.user_type == 2:  # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=user)
        return_data = {}
        return_data['total_up'] = 0
        return_data['total_down'] = 0
        return_data['rate_unit'] = 'byte'
        flow_data = []
        for i in sites:
            list_info = json.loads(i.flow_data)[::-1]
            for j in range(0, len(list_info)):
                try:
                    flow_data[j]['up'] += list_info[j]['up']
                    flow_data[j]['down'] += list_info[j]['down']
                    return_data['total_up'] += list_info[j]['up']
                    return_data['total_down'] += list_info[j]['down']
                except:
                    flow_data.append(list_info[j])
                    return_data['total_up'] += list_info[j]['up']
                    return_data['total_down'] += list_info[j]['down']
        return_data['flow_data'] = flow_data[::-1]
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
        site_flow['flow_data'] = json.loads(site_flow['flow_data'])
        return_data['site_flow'] = site_flow
        eq_flows = []
        for eq in eqs_info:
            eq_serializer = EquipmentFlowSerializer(instance=eq)
            data = copy(eq_serializer.data)
            data['flow_data'] = json.loads(data['flow_data'])
            eq_flows.append(data)

        return_data['eq_flows'] = eq_flows

        return Response(return_data, status=status.HTTP_200_OK)

