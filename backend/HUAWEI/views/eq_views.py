from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site, Equipment
from HUAWEI.serializers import EquipmentSerializer
from rest_framework.permissions import IsAuthenticated

class EquipmentListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        pass
        '''
        site = Site.objects.filter(user=request.user.pk)
        if(int(pk) >= len(site)):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        thesite = site[int(pk)]
        eqs = Equipment.objects.filter(site=thesite.pk)
        serializer = Equipment(instance=eqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        '''

