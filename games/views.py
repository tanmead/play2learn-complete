from django.shortcuts import render
import json
from .models import GameTracking
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

def record_score(request):
    data = json.loads(request.body)

    game = data['game']
    game_settings = data['gameSettings']
    score = data['score']
    user = request.user

    game_tracking = GameTracking(game=game, game_settings=game_settings, score=score, user=user)
    game_tracking.save()