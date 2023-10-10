from rest_framework.response import Response
from .utils import RankingService, PointsRankingCalculator
from rest_framework import status
from rest_framework import generics
from .models import Ranking


class TeamViewSet(generics.GenericAPIView):
    """
    API endpoint that allows games view table.
    """

    def get(self, request):
        point = PointsRankingCalculator()
        rankings = RankingService(points_ranking_calculator=point).calculate_rankings()

        return Response(rankings, status=status.HTTP_200_OK)
