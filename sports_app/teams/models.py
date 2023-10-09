from django.db import models


# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"
        db_table = "teams"
