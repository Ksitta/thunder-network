# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.models import Site
from HUAWEI.serializers import SiteDetailSerializer
from rest_framework.permissions import IsAuthenticated

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
        serializer = SiteDetailSerializer(instance=thesite)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        site = Site.objects.filter(user=request.user.pk)
        if(int(pk) >= len(site)):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        thesite = site[int(pk)]
        #华为那边也应该删除？ 未完成
        thesite.delete()
        return Response(status=status.HTTP_200_OK)
