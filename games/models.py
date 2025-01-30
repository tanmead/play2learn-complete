from django.db import models
from django.conf import settings

# Create your models here.
class GameTracking(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    game = models.CharField(max_length=100)
    game_settings = models.CharField(max_length=100)
    score = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )