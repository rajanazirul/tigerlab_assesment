from rest_framework.response import Response
from .utils import RankingService, PointsRankingCalculator
from rest_framework import status
from rest_framework import generics


class TeamViewSet(generics.GenericAPIView):

    def get(self, request):
        point = PointsRankingCalculator()
        rankings = RankingService(points_ranking_calculator=point).calculate_rankings()

        return Response(rankings, status=status.HTTP_200_OK)
