from rest_framework.serializers import ModelSerializer
from .models import Ranking, Team
from rest_framework import serializers


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ["name"]
        read_only_fields = fields


class RankingSerializer(ModelSerializer):
    team = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Ranking
        fields = ["team", "points"]
