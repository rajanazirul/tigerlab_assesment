from django.db import models


# Create your models here.
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
