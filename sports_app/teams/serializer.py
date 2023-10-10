from rest_framework.serializers import ModelSerializer
from .models import Ranking


class RankingSerializer(ModelSerializer):
    class Meta:
        model = Ranking
        fields = ["__all__"]
