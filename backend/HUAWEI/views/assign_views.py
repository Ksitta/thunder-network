# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment, User
from rest_framework.permissions import IsAuthenticated
from copy import copy
import datetime


class AssignView(APIView):
    """
    运营工程师将订单分配给网络工程师
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = self.request.user
        if user.user_type == 1:  # 运营工程师
            sites = Site.objects.all()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if(int(pk) >= len(sites)):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        thesite = sites[int(pk)]
        data = {}

        # 对于运营工程师，返回网络工程师列表
        if user.user_type == 1 and thesite.status == 1:
            networkers = User.objects.filter(user_type=2)
            data['networks'] = []
            for n in networkers:
                data['networks'].append(n.username)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        user = self.request.user
        network_name = self.request.data['network_name']
        if user.user_type == 1: # 运营工程师
            sites = Site.objects.all()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        thesite = sites[int(pk)]

        if thesite.status == 1 and user.user_type == 1:
            thesite.status = 2
            thesite.manager_name = user.username
            thesite.manager_time = datetime.datetime.now()
            thesite.network_name = network_name
            # 分配给网络工程师
            thesite.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
