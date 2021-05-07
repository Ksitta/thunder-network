# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Ticket, User
from HUAWEI.serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from copy import deepcopy
import datetime

class TicketView(APIView):
    queryset = Site.objects.all()
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        if user.user_type == 0:  # 用户
            tickets = Ticket.objects.filter(user=user)
        elif user.user_type == 2:  # 网络工程师
            tickets = Ticket.objects.filter(network_name=user.username)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TicketSerializer(instance=tickets, many=True)

        return_data = []
        data_list = serializer.data
        for i in range(0, len(data_list)):
            data = data_list[i]
            data['user'] = User.objects.get(pk=data['user']).username
            return_data.append(data)
        return Response(return_data, status=status.HTTP_200_OK)

    def post(self, request):
        data = deepcopy(self.request.data)
        user = self.request.user

        if user.user_type != 0:  # 身份不是用户
            return Response(status=status.HTTP_403_FORBIDDEN)

        sites = Site.objects.filter(user=user, site_name=data['site_name'])
        if len(sites) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        site = sites[0]
        item = {'status': 1,
                'user': self.request.user.pk,
                'network_name': site.network_name}
        data.update(item)
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request):
        data = deepcopy(self.request.data)
        user = self.request.user
        ticket = Ticket.objects.filter(id=int(data['id']))[0]
        if user.user_type == 0:  # 用户
            if ticket.status == 2:
                ticket.status = 0
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            ticket.close_time = datetime.datetime.now()
        elif user.user_type == 2:  # 网络工程师
            if ticket.status == 1:
                ticket.status = 2
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            ticket.answer = data['answer']
            ticket.network_time = datetime.datetime.now()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        ticket.save()
        return Response(status=status.HTTP_200_OK)