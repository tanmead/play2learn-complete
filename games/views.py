import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import GameTracking
from django.views.generic import TemplateView, ListView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class GameTrackingListView(ListView):
    model = GameTracking
    paginate_by = 10
    context_object_name = 'gametracking_list'

    def get_template_names(self):
        if "leaderboard" in self.request.path:
            return 'games/gametracking_leaderboard.html'
        return 'games/gametracking_list.html'

    def get_queryset(self):
        if "leaderboard" in self.request.path:
            qs = GameTracking.objects.all().order_by('-score')

            if "math-facts" in self.request.path:
                qs = qs.filter(game='Math Facts')

            elif "anagram-hunt" in self.request.path:
                qs = qs.filter(game='Anagram Hunt')

        else:
            qs = GameTracking.objects.filter(user=self.request.user).order_by('-time')

            if "math-facts" in self.request.path:
                qs = qs.filter(game='Math-Facts')

            elif "anagram-hunt" in self.request.path:
                qs = qs.filter(game='Anagram Hunt')

        return qs

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