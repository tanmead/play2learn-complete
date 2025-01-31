from django.urls import path

from games.views import MathFactsView, AnagramHuntView, GameTrackingListView, record_score

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('math-facts/<username>', GameTrackingListView.as_view(), name='math-facts-tracking'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('anagram-hunt/<username>', GameTrackingListView.as_view(), name='anagram-hunt-tracking'),
    path('record-score/', record_score, name='record-score'),
]