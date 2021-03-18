from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Equipment
from HUAWEI.serializers import EquipmentSerializers
from rest_framework.permissions import IsAuthenticated

class EquipmentListView(APIView):

    queryset = Equipment.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass


class SiteDetailView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        pass
