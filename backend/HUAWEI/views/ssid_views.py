from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, SSID, SSIDAuth
from HUAWEI.serializers import SSIDSerializer, SSIDAuthSerializer
from rest_framework.permissions import IsAuthenticated
from .nce import create_ssid
import datetime
from copy import deepcopy

class SSIDView(APIView):
    permission_classes = [IsAuthenticated]
    # def get(self, request, pk):
    #     pass

    def post(self, request, pk):
        user = self.request.user
        ssid_data = deepcopy(self.request.data)
        ssidAuth = self.request.data['ssidAuth']
        ssid_data.pop('ssidAuth', None)

        if user.user_type == 1:  # 运营工程师
            sites = Site.objects.all()
        elif user.user_type == 2:  # 网络工程师
            sites = Site.objects.filter(network_name=user.username)
        else:
            sites = Site.objects.filter(user=user)
        thesite = sites[int(pk)]

        if thesite.status == 1 or thesite.status == 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 与NCE通信
        # create_ssid_response = create_ssid(thesite.site_id, self.request.data)  #避免不同客户有相同的站点名
        # if create_ssid_response == IndexError:
        #     return Response("SSID重复！", status=status.HTTP_400_BAD_REQUEST)

        # 测试用
        create_ssid_response = str(pk) + user.username
        ssid_id = create_ssid_response

        # 在数据库中更新
        ssid_data['SSID_id'] = ssid_id
        ssid_data['site'] = thesite.pk
        ssid_serializer = SSIDSerializer(data=ssid_data)

        if ssid_serializer.is_valid():
            ssid_serializer.save()
        else:
            return Response(ssid_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ssidAuth['SSID'] = SSID.objects.get(SSID_id = ssid_id).pk
        ssidAuth_serializer = SSIDAuthSerializer(data=ssidAuth)
        if ssidAuth_serializer.is_valid():
            ssidAuth_serializer.save()
        return Response(status=status.HTTP_201_CREATED)

