from django.urls import path

from .views import HomePageView, ContactUsView, ContactUsThanksView, CreateReviewView, ReviewDetailView, ReviewDeleteView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('thanks/', ContactUsThanksView.as_view(), name='thanks'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/create/', CreateReviewView.as_view(), name='review-create'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]