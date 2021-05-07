from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment
from HUAWEI.serializers import EquipmentSerializer
from rest_framework.permissions import IsAuthenticated
import datetime

class EquipmentView(APIView):
    permission_classes = [IsAuthenticated]
    # def get(self, request, pk):
    #     pass

    def post(self, request, pk):
        user = self.request.user
        eq_num = self.request.data['eq_num']
        eq_list = self.request.data['eq_list']

        if user.user_type == 2: # 网络工程师
            sites = Site.objects.filter(network_name=user.username)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        thesite = sites[int(pk)]

        if thesite.status == 2 or thesite.status == 0:
            thesite.status = 0
            thesite.network_name = user.username
            thesite.network_time = datetime.datetime.now()
            thesite.save()

        # 在数据库中更新设备
        new_site = Site.objects.get(site_id = thesite.site_id)

        if len(Equipment.objects.filter(site = thesite.pk)) > 0:
            Equipment.objects.filter(site = thesite.pk).delete()

        for i in range(0, eq_num):
            eq_data = {
                'eq_id': str(new_site.pk) + str(i),
                'site': new_site.pk,
                'eq_name': eq_list[i]['eq_name'],
                'eq_status': int(eq_list[i]['eq_status'])
            }

            eq_serializer = EquipmentSerializer(data=eq_data)
            if eq_serializer.is_valid():
                eq_serializer.save()
            # else:
            #     return Response(eq_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

