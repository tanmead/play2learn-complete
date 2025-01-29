from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import ContactUsForm

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ContactUsView(FormView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('pages:thanks')

class ContactUsThanksView(TemplateView):
    template_name = 'pages/thanks.html'