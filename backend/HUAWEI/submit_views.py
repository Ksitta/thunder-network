from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Site
from .serializers import SiteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .nce import createSite
from copy import deepcopy

class SubmitOrderView(APIView):
    queryset = Site.objects.all()
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = deepcopy(self.request.data)
        """
        基础功能中，暂时自动为其生成AP设备、且自动返回订单成功
        之后应注意修改为，网络工程师同意后才成功
        """
        # 与华为交互
        # 获取site_id
        newsiteid = createSite(str(self.request.user.pk)+"-"+data['site_name']) #避免不同客户有相同的站点名
        # 创建站点ssid

        # 创建设备并更新设备信息表

        # 完成
        item = {'status': 1,
                'user': self.request.user.pk,
                'site_id': newsiteid}
        data.update(item)
        serializer = SiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

