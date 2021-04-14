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

        # new_site = Site.objects.get(site_id=thesite.site_id)
        # for i in range(0, eq_num):
        #     eq_data = {
        #         'eq_id': str(new_site.pk) + str(i),
        #         'site': new_site.pk,
        #         'eq_name': eq_list[i]['eq_name'],
        #         'eq_status': int(eq_list[i]['eq_status'])
        #     }
        #
        #     eq_serializer = EquipmentSerializer(data=eq_data)
        #     if eq_serializer.is_valid():
        #         eq_serializer.save()
        #     else:
        #         return Response(eq_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

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

