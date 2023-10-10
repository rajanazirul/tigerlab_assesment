from django.contrib import admin
from .models import Match


class MatchFilter(admin.ModelAdmin):
    list_display = [
        "id",
        "home_team_name",
        "home_score",
        "away_team_name",
        "home_score",
        "away_score",
        "updated_at",
    ]
    search_fields = ["home_team__name", "away_team__name", "created_at"]
    fields = ["home_team", "away_team", "home_score", "away_score"]

    def home_team_name(self, obj):
        return obj.home_team.name

    def away_team_name(self, obj):
        return obj.away_team.name


# Register your models here.
admin.site.register(Match, MatchFilter)
