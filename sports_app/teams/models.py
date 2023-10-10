from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"
        db_table = "teams"

    def __str__(self):
        return self.name


class Match(models.Model):
    home_team = models.ForeignKey(
        "teams.team",
        on_delete=models.CASCADE,
        related_name="home_team_match",
    )
    home_score = models.IntegerField()
    away_team = models.ForeignKey(
        "teams.team",
        on_delete=models.CASCADE,
        related_name="away_team_match",
    )
    away_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.home_team.name

    class Meta:
        verbose_name = "match"
        verbose_name_plural = "matches"
        db_table = "match"
        unique_together = ("home_team", "away_team")


class Ranking(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name = "ranking"
        verbose_name_plural = "rankings"
        db_table = "ranking"
