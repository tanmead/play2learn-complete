from django.contrib import admin
from common.admin import Play2LearnAdmin

from .models import GameTracking

# Register your models here.
@admin.register(GameTracking)
class GameTrackingAdmin(Play2LearnAdmin):
    model = GameTracking
    list_display = ['time', 'game', 'game_settings', 'score', 'user']
    ordering = ['-time']