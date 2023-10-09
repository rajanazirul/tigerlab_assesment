from django.db import models


# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=255, unique=True)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"
        db_table = "teams"


class Match(models.Model):
    home_team = models.ForeignKey(
        "teams.teams",
        on_delete=models.CASCADE,
        related_name="teams_match",
    )
    home_score = models.IntegerField()
    away_team = models.ForeignKey(
        "teams.teams",
        on_delete=models.CASCADE,
        related_name="teams_match",
    )
    away_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "match"
        verbose_name_plural = "matches"
        db_table = "match"
