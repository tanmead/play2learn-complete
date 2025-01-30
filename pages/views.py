import html
from django.views.generic import TemplateView, FormView, CreateView, DetailView, DeleteView, ListView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from common.utils.email import send_email
from .forms import ContactUsForm, ReviewForm
from .models import Review

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context

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

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'pages/review_detail.html'
    context_object_name = 'review'

class ReviewListView(ListView):
    model = Review

class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('pages:homepage')

    def test_func(self):
        review = self.get_object()
        return review.user == self.request.user