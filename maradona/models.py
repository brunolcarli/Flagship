from django.db import models


class MaradonaScore(models.Model):
    player_name = models.CharField(max_length=100, null=False, blank=False)
    steps = models.IntegerField(null=False)
    game_datetime = models.DateTimeField(auto_now_add=True)
