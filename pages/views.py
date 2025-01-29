import html
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from django.urls import reverse_lazy

from common.utils.email import send_email
from .forms import ContactUsForm, ReviewForm
from .models import Review

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ContactUsView(FormView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('pages:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'tannermeadtv@gmail.com'
        subject = 'Contact Us Form Submission'
        content = f'''
            <p>You have received a contact form submission:</p>
            <ol>
            '''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li><strong>{label}:</strong> {entry}</li>'

        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactUsThanksView(TemplateView):
    template_name = 'pages/thanks.html'

class CreateReviewView(CreateView):
    model = Review
    form_class = ReviewForm

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'pages/review_detail.html'
    context_object_name = 'review'