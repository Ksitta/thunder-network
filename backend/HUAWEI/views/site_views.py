# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment
from HUAWEI.serializers import SiteDetailSerializer, EquipmentDetailSerializer
from rest_framework.permissions import IsAuthenticated
# from HUAWEI.views.nce import delete_site
from copy import copy

class SiteListView(APIView):
    queryset = Site.objects.all()
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        if user.user_type == 1 or user.user_type == 2: # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=user)
        serializer = SiteDetailSerializer(instance=sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SiteDetailView(APIView):
    """
    获取或删除一个 site。 还没写好
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        user = self.request.user
        if user.user_type == 1 or user.user_type == 2: # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=request.user.pk)
        if(int(pk) >= len(sites)):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        thesite = sites[int(pk)]
        serializer = SiteDetailSerializer(instance=thesite)
        data = copy(serializer.data)


        if thesite.status == 1: #未完成订单，不返回设备信息
            pass
        else:   # 已完成订单 返回设备详细状态
            eqs = Equipment.objects.filter(site=thesite.pk)
            eqs_serializer = EquipmentDetailSerializer(instance=eqs, many=True)
            item = {'eqs': eqs_serializer.data}
            data.update(item)

        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.request.user
        if user.user_type == 1 or user.user_type == 2: # 运营&网络工程师
            sites = Site.objects.all()
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        thesite = sites[int(pk)]
        # serializer = SiteDetailSerializer(instance=thesite)

        if thesite.status == 1 and user.user_type == 1:
            thesite.status = 2
            thesite.save()
        elif thesite.status == 2 and user.user_type == 2:
            thesite.status = 0
            thesite.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = self.request.user
        if user.user_type == 1 or user.user_type == 2: # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=request.user.pk)
        if(int(pk) >= len(sites)):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        thesite = sites[int(pk)]
        eqs = Equipment.objects.filter(site=thesite.pk)

        # 与华为交互 删除站点
        # print("thesite.site_id: ", thesite.site_id)
        # delete_site_site_response = delete_site(thesite.site_id)
        # if delete_site_site_response == False:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # 从数据库中删除
        thesite.delete()
        # 与华为交互 删除设备 待完成

        # 从数据库中删除
        eqs.delete()
        # 删除流量表 待完成

        return Response(status=status.HTTP_204_NO_CONTENT)
