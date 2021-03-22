# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment
from HUAWEI.serializers import SiteDetailSerializer, EquipmentDetailSerializer
from rest_framework.permissions import IsAuthenticated
from HUAWEI.views.nce import delete_site
from copy import copy

class SiteListView(APIView):
    queryset = Site.objects.all()
    permission_classes = [IsAuthenticated]
    def get(self, request):
        sites = Site.objects.filter(user=request.user.pk)
        serializer = SiteDetailSerializer(instance=sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SiteDetailView(APIView):
    """
    获取或删除一个 site。 还没写好
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        site = Site.objects.filter(user=request.user.pk)
        if(int(pk) >= len(site)):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        thesite = site[int(pk)]
        eqs = Equipment.objects.filter(site=thesite.pk)
        serializer = SiteDetailSerializer(instance=thesite)
        eqs_serializer = EquipmentDetailSerializer(instance=eqs, many=True)

        data = copy(serializer.data)
        item = {'eqs': eqs_serializer.data}
        data.update(item)

        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        site = Site.objects.filter(user=request.user.pk)
        if(int(pk) >= len(site)):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        thesite = site[int(pk)]
        eqs = Equipment.objects.filter(site=thesite.pk)

        # 与华为交互 删除站点
        delete_site(thesite.site_id)
        # 从数据库中删除
        thesite.delete()
        # 与华为交互 删除设备 待完成

        # 从数据库中删除
        eqs.delete()

        # 删除流量表 待完成

        return Response(status=status.HTTP_200_OK)
