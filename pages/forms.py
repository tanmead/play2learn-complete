from django import forms
from django.forms import ModelForm

from .models import Review

class ContactUsForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}),
        help_text='Enter your message here.'
    )

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'review']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'review': 'Review',
        }
        help_texts = {
            'review': 'Enter your review here.'
        }