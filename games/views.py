from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import GameTracking
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

def record_score(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            # Process the data (e.g., save the score to the database)
            game = data['game']
            game_settings = data['game_settings']
            score = data['score']
            user = request.user

            game_tracking = GameTracking.objects.create(
                game=game,
                game_settings=game_settings,
                score=score,
                user=user
            )
            # Return a success response
            return JsonResponse({"status": "success", "message": "Score recorded successfully"})

        except Exception as e:
            # Handle other unexpected errors
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        # Handle non-POST requests
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed"}, status=405)