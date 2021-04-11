# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, User
from HUAWEI.serializers import SiteSerializer, SiteDetailSerializer, EquipmentDetailSerializer, EquipmentSerializer
from rest_framework.permissions import IsAuthenticated
from HUAWEI.views.nce import create_site
# from HUAWEI.views.nce import delete_site
from copy import copy, deepcopy
import time

class SiteView(APIView):
    queryset = Site.objects.all()
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        if user.user_type == 1 or user.user_type == 2:
            # 运营&网络工程师
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(user=user)
        serializer = SiteDetailSerializer(instance=sites, many=True)
        ret = []
        tem = serializer.data
        for i in range(0, len(tem)):
            t = tem[i]
            t['user'] = User.objects.get(pk=t['user']).username
            ret.append(t)
        return Response(ret, status=status.HTTP_200_OK)

    def post(self, request):
        data = deepcopy(self.request.data)
        """
        基础功能中，暂时自动为其生成AP设备、且自动返回订单成功
        之后应注意修改为，网络工程师同意后才成功
        """
        # 与华为交互 创建Site
          ### 获取site_id
        #create_site_response = create_site(str(self.request.user.username) + str(self.request.user.pk)+"-"+data['site_name']) #避免不同客户有相同的站点名
        #if create_site_response == IndexError:
        #    return Response("站点名称重复！", status=status.HTTP_400_BAD_REQUEST)

        # 测试用
        create_site_response = str(self.request.user.pk) + "-" + data['site_name'] + str(time.time())
        new_site_id = create_site_response

          ### 创建站点ssid 待完成 华为交互？？？

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
        return Response(status=status.HTTP_201_CREATED)

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


        if thesite.status == 0: # 已完成订单 返回设备详细状态 未完成订单，不返回设备信息
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
            return Response(status=status.HTTP_403_FORBIDDEN)
        thesite = sites[int(pk)]

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
            return Response(status=status.HTTP_403_FORBIDDEN)
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
