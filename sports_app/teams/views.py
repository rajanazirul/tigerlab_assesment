from rest_framework.response import Response
from .serializer import RankingSerializer
from .models import Ranking
from rest_framework import status
from rest_framework.views import APIView


class TeamViewSet(APIView):
    serializer_class = RankingSerializer

    def get(self, request):
        rankings = Ranking.objects.all().order_by('-points', 'team')

        serializer = self.serializer_class(data=rankings)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
