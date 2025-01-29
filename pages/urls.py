from django.urls import path

from .views import HomePageView, ContactUsView, ContactUsThanksView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('thanks/', ContactUsThanksView.as_view(), name='thanks'),
]