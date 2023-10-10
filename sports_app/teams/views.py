from rest_framework.response import Response
from .serializer import RankingSerializer
from .utils import RankingService, PointsRankingCalculator
from .models import Ranking
from rest_framework import status
from rest_framework.views import APIView


class TeamViewSet(APIView):
    serializer_class = RankingSerializer

    def get(self, request):
        point = PointsRankingCalculator()
        rankings = RankingService(points_ranking_calculator=point).calculate_rankings()

        serializer = self.serializer_class(data=rankings)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
