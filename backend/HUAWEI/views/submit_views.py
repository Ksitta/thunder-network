# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site
from HUAWEI.serializers import SiteSerializer, EquipmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from HUAWEI.views.nce import create_site
from copy import deepcopy
import time

class SubmitOrderView(APIView):
    queryset = Site.objects.all()
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = deepcopy(self.request.data)
        """
        基础功能中，暂时自动为其生成AP设备、且自动返回订单成功
        之后应注意修改为，网络工程师同意后才成功
        """
        # 与华为交互 创建Site
          ### 获取site_id
        create_site_response = create_site(str(self.request.user.username) + str(self.request.user.pk)+"-"+data['site_name']) #避免不同客户有相同的站点名
        if create_site_response == IndexError:
            return Response("站点名称重复！", status=status.HTTP_400_BAD_REQUEST)
        new_site_id = create_site_response
        # new_site_id = str(self.request.user.pk)+"-"+"site"
          ### 创建站点ssid 待完成

        # 在数据库中更新Site表
        item = {'status': 1,
                'user': self.request.user.pk,
                'site_id': new_site_id}
        data.update(item)

        serializer = SiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 与华为交互 创建设备 待完成

        # 在数据库中更新设备
        new_site = Site.objects.get(site_id=new_site_id)
        eq_data1 = {
            'eq_id': str(new_site.pk) + "111",
            'site': new_site.pk,
            'eq_name': "ap1",
            'eq_status': 1
        }
        eq_data2 = {
            'eq_id': str(new_site.pk) + "222",
            'site': new_site.pk,
            'eq_name': "ap2",
            'eq_status': 1
        }
        eq1_serializer = EquipmentSerializer(data=eq_data1)
        eq2_serializer = EquipmentSerializer(data=eq_data2)
        if eq1_serializer.is_valid() and eq2_serializer.is_valid():
            eq1_serializer.save()
            eq2_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(eq1_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

