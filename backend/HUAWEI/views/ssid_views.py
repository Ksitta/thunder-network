from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, SSID, SSIDAuth
from HUAWEI.serializers import SSIDSerializer, SSIDAuthSerializer
from rest_framework.permissions import IsAuthenticated
from .nce import create_ssid, delete_ssid
from copy import deepcopy

class SSIDView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        user = self.request.user
        if user.user_type == 1:  # 运营工程师
            sites = Site.objects.all()
        elif user.user_type == 2:  # 网络工程师
            sites = Site.objects.filter(network_name=user.username)
        else:
            sites = Site.objects.filter(user=user)
        thesite = sites[int(pk)]

        if thesite.status == 1 or thesite.status == 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        theSSID = SSID.objects.get(site=thesite.pk)
        SSID_serializer = SSIDSerializer(instance=theSSID)
        theSSIDAuth = SSIDAuth.objects.get(SSID=theSSID.pk)
        SSIDAuth_serializer = SSIDAuthSerializer(instance=theSSIDAuth)
        return_data = SSID_serializer.data
        return_data['ssidAuth'] = SSIDAuth_serializer.data

        return Response(return_data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        user = self.request.user
        ssid_data = deepcopy(self.request.data)
        ssidAuth = self.request.data['ssidAuth']
        ssid_data.pop('ssidAuth', None)

        if user.user_type == 1 or user.user_type == 2:  # 运营工程师/网络工程师
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            sites = Site.objects.filter(user=user)
        thesite = sites[int(pk)]

        if thesite.status == 1 or thesite.status == 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 数据格式校验
        if ssidAuth['pskEncryptType'] == "wep":
            if ssidAuth['mode'] == "ppsk":
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if len(ssidAuth['securityKey']) != 5:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            if len(ssidAuth['securityKey']) < 8:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        if len(SSID.objects.filter(site=thesite.pk)) > 0: # 若已有SSID则先删掉（即进行修改）
            before_ssid = SSID.objects.get(site=thesite.pk)

            # 与NCE通信删除ssid
            delete_ssid_response = delete_ssid(thesite.site_id, before_ssid.SSID_id)
            if delete_ssid_response == KeyError:
                return Response("SSID重复！", status=status.HTTP_400_BAD_REQUEST)
            elif delete_ssid_response == before_ssid.SSID_id:
                SSID.objects.filter(site=thesite.pk).delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        # 与NCE通信
        create_ssid_response = create_ssid(thesite.site_id, self.request.data)  #避免不同客户有相同的站点名
        if create_ssid_response == KeyError:
            return Response("SSID重复！", status=status.HTTP_400_BAD_REQUEST)

        # 测试用
        # create_ssid_response = str(pk) + user.username
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

